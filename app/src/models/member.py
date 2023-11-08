from src.models.check_member import CheckMember
from src.models.points import Points
from src.models.register import Register
from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from sqlalchemy import String, Date
from typing import List
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Member(BaseIdModel, BaseTimeModel):
    __tablename__ = "member"

    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    nickname: Mapped[str] = mapped_column(String(120), nullable=True)
    surname: Mapped[str] = mapped_column(String(120), nullable=False)
    mobile: Mapped[str] = mapped_column(String(120), nullable=True)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    address: Mapped[str] = mapped_column(String(120), nullable=True)
    birth_date: Mapped[str] = mapped_column(Date(), nullable=True)

    # 1:N
    register: Mapped[List["Register"]] = relationship(back_populates="member")

    # 1:1
    user: Mapped["User"] = relationship(uselist=False, back_populates="member")

    points: Mapped[List["Points"]] = relationship(back_populates="member")

    check_meets: Mapped[List["CheckMember"]] = relationship(back_populates="member")
