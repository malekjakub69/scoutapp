import re
from typing import Type
from src.models import db
from src.models.base import BaseIdModel, T
from werkzeug.exceptions import BadRequest
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from src.translations.translator import Translator


class User(BaseIdModel):
    """
    Represents a user in the system.

    Attributes:
        email (str): The user's email address.
        login (str): The user's login name.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        last_login (datetime): The date and time of the user's last login.
        roles (List[Role]): The roles assigned to the user.
        current_unit (Unit): The user's current unit.
        person (Person): The person associated with the user.
    """

    __tablename__ = "user"

    email = db.Column(db.String(120), unique=True, nullable=False)
    login = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(240), nullable=False)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=True)
    last_login = db.Column(db.DateTime, nullable=True)
    registration_date = db.Column(db.DateTime, default=db.func.now())

    # 1:N
    ## Have role
    permissions = db.relationship("Permission", back_populates="user")

    ## Current unit
    current_unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=True)
    current_unit = db.relationship("Unit", back_populates="users", uselist=False)

    # 1:1
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    person = db.relationship("Person", back_populates="user", uselist=False)

    @classmethod
    def verify_password(cls, original_hash: str, password: str) -> bool:
        return check_password_hash(original_hash, password)

    @classmethod
    def get_by_email_or_login(cls: Type[T], id_string: str) -> T:
        id_string = id_string.lower()
        user = cls.query.filter(or_(User.email == id_string, User.login == id_string)).first()
        return user

    @classmethod
    def hash_password(cls, password: str) -> str:
        cls._validate_password(password)
        return generate_password_hash(password)

    @classmethod
    def _validate_password(cls, value: str) -> None:
        if len(value) < 8:
            raise BadRequest(Translator.localize("short_password"))
        elif re.search(r"[0-9]", value) is None:
            raise BadRequest(Translator.localize("number_not_in_password"))
        elif re.search(r"[A-Z]", value) is None:
            raise BadRequest(Translator.localize("capital_not_in_password"))
