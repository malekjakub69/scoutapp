from src.models.check_member import CheckMember
from src.models.points import Points
from src.models.base import BaseIdModel, BaseTimeModel, T
from typing import List
import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Meet(BaseIdModel, BaseTimeModel):
    __tablename__ = "meet"

    date: Mapped[datetime.date] = mapped_column(Date(), nullable=False)
    type: Mapped[str] = mapped_column(String(60), nullable=False)
    photograpy_url: Mapped[str] = mapped_column(String(240), nullable=True)

    points: Mapped[List["Points"]] = relationship(back_populates="meet")

    check_members: Mapped[List["CheckMember"]] = relationship(
        back_populates="check_member"
    )

    troop: Mapped["Troop"] = relationship(back_populates="meets")
    troop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("troop.id"))
