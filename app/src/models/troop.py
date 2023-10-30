from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T


class Troop(BaseIdModel, BaseTimeModel):
    __tablename__ = "troop"

    name = db.Column(db.String(120), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    code = db.Column(
        db.Integer,
        nullable=False,
        unique=True,
    )

    # self 1:N
    ## Troop hierarchy
    troop = db.relationship("Troop", remote_side=[id])
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"))

    # 1:N
    ## Current troop
    users = db.relationship("User", back_populates="current_troop")
    ## Role in troop
    roles = db.relationship("Role", back_populates="troop")
    ## Register in troop
    register = db.relationship("Register", back_populates="troop")

    meets = db.relationship("Meet", back_populates="troop")
