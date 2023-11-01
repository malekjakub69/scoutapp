from datetime import datetime
from typing import Type, TypeVar
from urllib.parse import unquote
from sqlalchemy.orm import Mapped
from sqlalchemy import Integer, DateTime

from sqlalchemy.orm import DeclarativeBase
from src.models import db
from sqlalchemy.orm import mapped_column

T = TypeVar("T", bound="BaseModel")


class BaseModel(DeclarativeBase):
    __abstract__ = True

    def __str__(self):
        return self.to_dict()


class BaseIdModel(BaseModel):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)

    @classmethod
    def base_sort(cls) -> list:
        return [cls.id.desc()]

    @classmethod
    def get_by_id(cls: Type[T], id_: int) -> T:
        return cls.query.filter_by(id=id_).first()


class BaseTimeModel:
    __abstract__ = True

    created_on: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_on: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @classmethod
    def base_sort(cls) -> list:
        return [cls.created_on.desc()]
