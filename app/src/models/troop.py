from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T
from src.models.role import Role
from src.models.user import User


class Troop(BaseIdModel, BaseTimeModel):
    __tablename__ = "troop"

    name = db.Column(db.String(120), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # self 1:N
    ## Troop hierarchy
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=True)
    troop = db.relationship("Troop", remote_side=[id])

    # 1:N
    ## Current troop
    users: User = db.relationship("User", back_populates="current_troop")
    ## Role in troop
    roles: Role = db.relationship("Role", uselist=False, back_populates="troop")
