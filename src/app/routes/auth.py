import logging

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from src.app.config import settings
from src.app.db.models.models import UsersORM
from src.app.models.auth import LoginRequest, SignupRequest, UserResponse
from src.app.services import auth

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/signup")
def signup(user_data: SignupRequest, db: Session = Depends(get_db)) -> UserResponse:
    # validate email shape, check if email already exists
    if not auth.verify_email_shape(user_data.email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    if not user_data.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty")

    hashed_password = auth.hash_password(user_data.password)

    # Check if email already exists
    existing = db.execute(
        select(UsersORM).where(UsersORM.email == user_data.email)
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Insert new user
    user = UsersORM(
        name=user_data.name, email=user_data.email, password_hash=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    user_id = user.id
    if user_id is None:
        raise RuntimeError("Failed to retrieve inserted user id.")

    logger.info(f"User created with ID: {user_id}")

    return UserResponse(id=user_id, name=user_data.name, email=user_data.email)


@router.post("/login")
def login(
    login_data: LoginRequest, response: Response, db: Session = Depends(get_db)
) -> dict[str, bool]:
    if not auth.verify_email_shape(login_data.email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    user = db.execute(
        select(UsersORM).where(UsersORM.email == login_data.email)
    ).scalar_one_or_none()

    if not user or not auth.verify_password(
        login_data.password,
        user.password_hash,
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token(user.id)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=not settings.debug_mode,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,
    )
    logger.info(f"User logged in with ID: {user.id}")

    return {"success": True}


@router.post("/logout")
def logout(
    response: Response, user: UserResponse = Depends(auth.get_current_user)
) -> dict[str, bool]:
    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=not settings.debug_mode,
        samesite="lax",
    )
    logger.info(f"Current user logged out with ID: {user.id}")
    return {"success": True}


@router.get("/me")
def me(user: UserResponse = Depends(auth.get_current_user)) -> UserResponse:
    logger.info(f"Fetching user info for ID: {user.id}")
    return user
