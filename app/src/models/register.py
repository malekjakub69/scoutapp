from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel


class Register(BaseIdModel, BaseTimeModel):
    """
    Represents a registration of a member to a troop.

    Attributes:
        member_id (int): The ID of the member being registered.
        member (Member): The member being registered.
        troop_id (int): The ID of the troop the member is being registered to.
        troop (Troop): The troop the member is being registered to.
    """

    __tablename__ = "register"

    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    member = db.relationship("Member", back_populates="register")

    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=False)
    troop = db.relationship("Troop", back_populates="register")
