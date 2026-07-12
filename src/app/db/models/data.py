from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.db.models.base import Base


class DataORM(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
