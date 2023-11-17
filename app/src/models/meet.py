from src.models import db
from src.models.base import BaseTimeModel, BaseIdModel


class Meet(BaseIdModel, BaseTimeModel):
    """
    Represents a meeting of a scout troop.

    Attributes:
        date (date): The date of the meet.
        type (str): The type of the meet.
        photograpy_url (str): The URL of the photography for the meet.
        points (List[Points]): The points associated with the meet.
        check_members (List[CheckMember]): The check members associated with the meet.
        troop (Troop): The troop associated with the meet.
        troop_id (int): The ID of the troop associated with the meet.
    """

    __tablename__ = "meet"

    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(60), nullable=False)
    photograpy_url = db.Column(db.String(240), nullable=True)

    points = db.relationship("Points", back_populates="meet")

    check_members = db.relationship("CheckMember", back_populates="meet")

    troop = db.relationship("Troop", back_populates="meets")
    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=False)
