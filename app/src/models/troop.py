from src.models.meet import Meet
from src.models.register import Register
from src.models.role import Role
from src.models.user import User
from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Integer


class Troop(BaseIdModel, BaseTimeModel):
    __tablename__ = "troop"

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    number: Mapped[int] = mapped_column(Integer(), nullable=False)
    code: Mapped[int] = mapped_column(String(16), nullable=False, unique=True)

    # self 1:N
    ## Troop hierarchy
    troop: Mapped[List["Troop"]] = relationship(back_populates="troop")
    troop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("troop.id"))

    # 1:N
    ## Current troop
    users: Mapped[List["User"]] = relationship(back_populates="current_troop")
    ## Role in troop
    roles: Mapped[List["Role"]] = relationship(back_populates="troop")
    ## Register in troop
    register: Mapped[List["Register"]] = relationship(back_populates="troop")

    meets: Mapped[List["Meet"]] = relationship(back_populates="troop")
