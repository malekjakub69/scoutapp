from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer


class Points(BaseIdModel, BaseTimeModel):
    __tablename__ = "points"

    member: Mapped["Member"] = relationship(back_populates="points")
    member_id: Mapped[int] = mapped_column(Integer(), ForeignKey("member.id"))

    meet: Mapped["Meet"] = relationship(back_populates="points")
    meet_id: Mapped[int] = mapped_column(Integer(), ForeignKey("meet.id"))
