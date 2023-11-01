from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from typing import List
from datetime import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, DateTime, Integer


class User(BaseIdModel, BaseTimeModel):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    login: Mapped[str] = mapped_column(String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(240), nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    surname: Mapped[str] = mapped_column(String(120), nullable=False)
    last_login: Mapped[datetime] = mapped_column(DateTime(), nullable=True)

    # 1:N
    ## Have role
    roles: Mapped[List["Role"]] = relationship(back_populates="user")

    ## Current troop
    current_troop: Mapped["Troop"] = relationship(back_populates="users", uselist=False)
    current_troop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("troop.id"))

    # 1:1
    member: Mapped["Member"] = relationship(back_populates="user")
    member_id: Mapped[int] = mapped_column(Integer(), ForeignKey("member.id"))
