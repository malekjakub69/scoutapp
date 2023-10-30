from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel


class Role(BaseIdModel, BaseTimeModel):
    __tablename__ = "role"

    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    # 1:N
    ## Have role
    user = db.relationship("User", back_populates="roles")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ## Role in troop
    troop = db.relationship("Troop", back_populates="roles")
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"))

    @classmethod
    def get_role_id(cls, code: str) -> int:
        return cls.query.filter_by(code=code).first().id

    @classmethod
    def is_valid(cls, code: str) -> bool:
        return cls.query.filter_by(code=code).first() is not None
