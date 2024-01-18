from src.models import db
from src.models.base import BaseIdModel


class CheckMember(BaseIdModel):
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
        no_reason (str): The reason for not checking in.
        member_hash (str): The hash of the member's name.
    """

    __tablename__ = "check_member"

    member_hash = db.Column(db.String(32), unique=True, nullable=False)
    other_desc = db.Column(db.String, nullable=True)
    confirm = db.Column(db.Boolean, nullable=False)
    no_reason = db.Column(db.String(1024), nullable=True)
    sent = db.Column(db.Boolean, nullable=False, default=False)

    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=True)
    member = db.relationship("Member", back_populates="check_members")

    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"), nullable=False)
    meet = db.relationship("Meet", back_populates="check_members")

    @classmethod
    def get_by_member_hash(cls, member_hash: str):
        return cls.query.filter_by(member_hash=member_hash).first()
