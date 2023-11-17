from src.models import db
from src.models.base import BaseTimeModel, BaseIdModel


class CheckMember(BaseIdModel, BaseTimeModel):
    """
    Represents a check-in record for a member at a meet.

    Attributes:
        member_name (str): The name of the member who checked in.
        other_desc (str): Any additional description for the check-in record.
        confirm (bool): Whether the check-in was confirmed or not.
        member_id (int): The foreign key for the associated member.
        member (Member): The associated member object.
        meet_id (int): The foreign key for the associated meet.
        meet (Meet): The associated meet object.
    """

    __tablename__ = "check_member"

    member_name = db.Column(db.String, nullable=False)
    other_desc = db.Column(db.String, nullable=True)
    confirm = db.Column(db.Boolean, nullable=False)

    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=True)
    member = db.relationship("Member", back_populates="check_members")

    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"), nullable=False)
    meet = db.relationship("Meet", back_populates="check_members")
