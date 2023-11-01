from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer


class Register(BaseIdModel, BaseTimeModel):
    __tablename__ = "register"

    member: Mapped["Member"] = relationship(back_populates="register")
    member_id: Mapped[int] = mapped_column(Integer(), ForeignKey("member.id"))

    troop: Mapped["Troop"] = relationship(back_populates="register")
    troop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("troop.id"))
