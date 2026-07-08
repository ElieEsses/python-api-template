from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():
    return {"message": "Health check passed", "status": "ok"}
