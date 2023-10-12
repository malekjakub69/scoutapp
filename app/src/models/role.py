from typing import Type

from flask_restful import request
from sqlalchemy import or_
from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel


class Role(BaseIdModel, BaseTimeModel):
    __tablename__ = "role"

    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    # 1:N
    ## Have role
    user_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    user = db.relationship("User", back_populates="roles")
    ## Role in troop
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=False)
    troop = db.relationship("Troop", back_populates="roles")

    @classmethod
    def get_role_id(cls, code: str) -> int:
        return cls.query.filter_by(code=code).first().id

    @classmethod
    def is_valid(cls, code: str) -> bool:
        return cls.query.filter_by(code=code).first() is not None
