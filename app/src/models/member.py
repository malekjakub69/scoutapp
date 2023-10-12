from typing import Type

from flask_restful import request
from sqlalchemy import or_
from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel

from api.app.src.models.user import User


class Member(BaseIdModel, BaseTimeModel):
    __tablename__ = "member"

    name = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(120), nullable=True)
    surname = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(240), nullable=True)
    birthDate = db.Column(db.Date, nullable=True)

    # 1:N

    # 1:1
    user_id = db.mapped_column(db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="user")

    @classmethod
    def get_role_id(cls, code: str) -> int:
        return cls.query.filter_by(code=code).first().id

    @classmethod
    def is_valid(cls, code: str) -> bool:
        return cls.query.filter_by(code=code).first() is not None
