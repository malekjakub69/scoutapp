from src.models import db
from src.models.base import BaseIdModel


class Meet(BaseIdModel):
    """
    Represents a meeting of a scout unit.

    Attributes:
        date (date): The date of the meet.
        type (str): The type of the meet.
        photograpy_url (str): The URL of the photography for the meet.
        points (List[Points]): The points associated with the meet.
        check_persons (List[CheckPerson]): The check persons associated with the meet.
        unit (Unit): The unit associated with the meet.
        unit_id (int): The ID of the unit associated with the meet.
    """

    __tablename__ = "meet"

    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(60), nullable=False)
    photograpy_url = db.Column(db.String(240), nullable=True)

    points = db.relationship("Points", back_populates="meet")

    check_persons = db.relationship("CheckPerson", back_populates="meet")

    unit = db.relationship("Unit", back_populates="meets")
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=False)
