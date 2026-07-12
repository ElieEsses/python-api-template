from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.db.models import DataORM
from src.app.models.data import Data, UserData

router = APIRouter()


@router.get("/data")
def list_data(db: Session = Depends(get_db)) -> list[Data]:
    rows = db.execute(select(DataORM)).scalars().all()
    return [Data(id=row.id, title=row.title) for row in rows]


@router.post("/data")
def create_data(body: UserData, db: Session = Depends(get_db)) -> Data:
    data = DataORM(title=body.title)
    db.add(data)
    db.commit()
    db.refresh(data)
    return Data(id=data.id, title=data.title)
