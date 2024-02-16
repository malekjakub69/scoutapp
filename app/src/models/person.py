from src.models import db
from src.models.base import BaseIdModel


class Person(BaseIdModel):
    """
    Represents a person of the organization.

    Attributes:
        first_name (str): The first name of the person.
        nickname (str): The nickname of the person.
        last_name (str): The last name of the person.
        mobile (str): The mobile phone number of the person.
        email (str): The email address of the person.
        address (str): The address of the person.
        birth_date (datetime.date): The birth date of the person.
        register (List[Register]): The list of registers associated with the person.
        user (User): The user associated with the person.
        points (List[Points]): The list of points associated with the person.
        check_persons (List[CheckPerson]): The list of check persons associated with the person.
    """

    __tablename__ = "person"

    first_name = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    birth_date = db.Column(db.Date(), nullable=True)

    # 1:N
    register = db.relationship("Register", back_populates="person")

    # 1:1
    user = db.relationship("User", uselist=False, back_populates="person")

    points = db.relationship("Points", back_populates="person")

    check_persons = db.relationship("CheckPerson", back_populates="person")
