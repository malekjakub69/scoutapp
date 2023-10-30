from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, Date


class Member(BaseIdModel, BaseTimeModel):
    __tablename__ = "member"

    first_name = mapped_column(String(120), nullable=False)
    nickname = mapped_column(String(120), nullable=True)
    surname = mapped_column(String(120), nullable=False)
    mobile = mapped_column(String(120), nullable=True)
    email = mapped_column(String(120), nullable=True)
    address = mapped_column(String(120), nullable=True)
    birth_date = mapped_column(Date(), nullable=True)

    # 1:N
    register = db.relationship("Register", back_populates="member")

    # 1:1
    user = db.relationship("User", uselist=False, back_populates="member")

    points = db.relationship("Points", back_populates="member")

    check_meets = db.relationship("CheckMember", back_populates="member")

    @classmethod
    def get_role_id(cls, code: str) -> int:
        return cls.query.filter_by(code=code).first().id

    @classmethod
    def is_valid(cls, code: str) -> bool:
        return cls.query.filter_by(code=code).first() is not None
