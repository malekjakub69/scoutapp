from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel, T
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Meet(BaseIdModel, BaseTimeModel):
    __tablename__ = "meet"

    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    photograpy_url = db.Column(db.String(240), nullable=True)

    points = db.relationship("Points", back_populates="meet")

    check_members: Mapped[List["CheckMember"]] = relationship(back_populates="meet")

    troop = db.relationship("Troop", back_populates="meets")
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"))
