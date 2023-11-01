from src.models.base import BaseIdModel, BaseTimeModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Integer


class Role(BaseIdModel, BaseTimeModel):
    __tablename__ = "role"

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    code: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # 1:N
    ## Have role
    user: Mapped["User"] = relationship(back_populates="roles")
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey("user.id"))
    ## Role in troop
    troop: Mapped["Troop"] = relationship(back_populates="roles")
    troop_id: Mapped[int] = mapped_column(Integer(), ForeignKey("troop.id"))
