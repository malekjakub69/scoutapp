from src.models import db
from src.models.base import BaseIdModel


class Points(BaseIdModel):
    """
    Represents the points earned by a member in a meet.

    Attributes:
        point (int): The number of points earned by the member in the meet.
        member (Member): The member who earned the points.
        member_id (int): The ID of the member who earned the points.
        meet (Meet): The meet in which the points were earned.
        meet_id (int): The ID of the meet in which the points were earned.
    """

    __tablename__ = "points"

    point = db.Column(db.Integer)

    member = db.relationship("Member", back_populates="points")
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)

    meet = db.relationship("Meet", back_populates="points")
    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"), nullable=False)
