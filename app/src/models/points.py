from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T


class Points(BaseIdModel, BaseTimeModel):
    __tablename__ = "points"

    member = db.relationship("Member", back_populates="points")
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    meet = db.relationship("Meet", back_populates="points")
    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"))
