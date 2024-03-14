from src.models import db
from src.models.base import BaseIdModel


class CheckPerson(BaseIdModel):
    """
    Represents a check-in record for a person at a meet.

    Attributes:
        person_name (str): The name of the person who checked in.
        other_desc (str): Any additional description for the check-in record.
        confirm (bool): Whether the check-in was confirmed or not.
        person_id (int): The foreign key for the associated person.
        person (Person): The associated person object.
        meet_id (int): The foreign key for the associated meet.
        meet (Meet): The associated meet object.
        no_reason (str): The reason for not checking in.
        person_hash (str): The hash of the persons's name.
    """

    __tablename__ = "check_person"

    person_hash = db.Column(db.String(32), unique=True, nullable=False)
    other_desc = db.Column(db.String, nullable=True)
    confirm = db.Column(db.Boolean, nullable=False)
    no_reason = db.Column(db.String(1024), nullable=True)
    sent = db.Column(db.Boolean, nullable=False, default=False)

    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    person = db.relationship("Person", back_populates="check_persons")

    meet_id = db.Column(db.Integer, db.ForeignKey("meet.id"), nullable=False)
    meet = db.relationship("Meet", back_populates="check_persons")

    @classmethod
    def get_by_person_hash(cls, person_hash: str):
        return cls.query.filter_by(person_hash=person_hash).first()

    @classmethod
    def get_by_meet_id(cls, meet_id):
        return cls.query.filter_by(meet_id=meet_id).all()
