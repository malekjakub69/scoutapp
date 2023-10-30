from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T


class Register(BaseIdModel, BaseTimeModel):
    __tablename__ = "register"

    member = db.relationship("Member", back_populates="register")
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    troop = db.relationship("Troop", back_populates="register")
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"))
