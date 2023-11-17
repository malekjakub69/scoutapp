from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel


class User(BaseIdModel, BaseTimeModel):
    """
    Represents a user in the system.

    Attributes:
        email (str): The user's email address.
        login (str): The user's login name.
        password (str): The user's password.
        first_name (str): The user's first name.
        surname (str): The user's surname.
        last_login (datetime): The date and time of the user's last login.
        roles (List[Role]): The roles assigned to the user.
        current_troop (Troop): The user's current troop.
        member (Member): The member associated with the user.
    """

    __tablename__ = "user"

    email = db.Column(db.String(120), unique=True, nullable=False)
    login = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(240), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    last_login = db.Column(db.DateTime(), nullable=True)

    # 1:N
    ## Have role
    permissions = db.relationship("Permission", back_populates="user")

    ## Current troop
    current_troop = db.relationship("Troop", back_populates="users", uselist=False)
    current_troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=True)

    # 1:1
    member = db.relationship("Member", back_populates="user", uselist=False)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=True)
