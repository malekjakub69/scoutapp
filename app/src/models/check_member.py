from src.models.base import BaseIdModel, BaseTimeModel, T
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class CheckMember(BaseIdModel, BaseTimeModel):
    __tablename__ = "check_member"

    member_name: Mapped[str] = mapped_column(nullable=False)
    other_desc: Mapped[str] = mapped_column(nullable=True)
    confirm: Mapped[bool] = mapped_column(nullable=False)

    member_id: Mapped[int] = mapped_column(ForeignKey("member.id"))
    member: Mapped["Member"] = relationship(back_populates="check_members")

    meet_id: Mapped[int] = mapped_column(ForeignKey("meet.id"))
    meet: Mapped["Meet"] = relationship(back_populates="check_meets")
