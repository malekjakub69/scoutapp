from src.models import db
from src.models.base import BaseIdModel


class Member(BaseIdModel):
    """
    Represents a member of the organization.

    Attributes:
        first_name (str): The first name of the member.
        nickname (str): The nickname of the member.
        last_name (str): The last name of the member.
        mobile (str): The mobile phone number of the member.
        email (str): The email address of the member.
        address (str): The address of the member.
        birth_date (datetime.date): The birth date of the member.
        register (List[Register]): The list of registers associated with the member.
        user (User): The user associated with the member.
        points (List[Points]): The list of points associated with the member.
        check_members (List[CheckMember]): The list of check members associated with the member.
    """

    __tablename__ = "member"

    first_name = db.Column(db.String(120), nullable=False)
    nickname = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    birth_date = db.Column(db.Date(), nullable=True)

    # 1:N
    register = db.relationship("Register", back_populates="member")

    # 1:1
    user = db.relationship("User", uselist=False, back_populates="member")

    points = db.relationship("Points", back_populates="member")

    check_members = db.relationship("CheckMember", back_populates="member")
