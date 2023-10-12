from typing import Type

from flask_restful import request
from sqlalchemy import or_
from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T
from src.models.role import Role


class User(BaseIdModel, BaseTimeModel):
    __tablename__ = "user"

    email = db.Column(db.String(120), unique=True, nullable=False)
    login = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120), nullable=True)
    first_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    # 1:N
    ## Have role
    role: Role = db.relationship("Role", uselist=False, back_populates="user")
    ## Current troop
    current_troop = db.relationship("Troop", back_populates="users", uselist=False)

    # 1:1

    member = db.relationship("Member", uselist=False, back_populates="user")

    @classmethod
    def get_by_email_or_login(cls: Type[T], id_string: str, set_language=True) -> T:
        id_string = id_string.lower()
        user = cls.query.filter(or_(User.email == id_string, User.login == id_string)).first()
        if set_language and user:
            request.__setattr__("language", user.resolve_language())
        return user
