from src.models import db
from src.models.base import BaseIdModel


class Points(BaseIdModel):
    """
    Represents the points earned by a person in a meet.

    Attributes:
        point (int): The number of points earned by the person in the meet.
        person (Person): The person who earned the points.
        person_id (int): The ID of the person who earned the points.
        meet (Meet): The meet in which the points were earned.
        meet_id (int): The ID of the meet in which the points were earned.
    """

    __tablename__ = "points"

    point = db.Column(db.Integer)

    person = db.relationship("Person", back_populates="points")
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)

    meet = db.relationship("Meet", back_populates="points")
    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"), nullable=False)
