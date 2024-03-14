from src.models import db
from src.models.base import BaseIdModel


class Register(BaseIdModel):
    """
    Represents a registration of a person to a unit.

    Attributes:
        person_id (int): The ID of the person being registered.
        person (Person): The person being registered.
        unit_id (int): The ID of the unit the person is being registered to.
        unit (Unit): The unit the person is being registered to.
    """

    __tablename__ = "register"

    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    person = db.relationship("Person", back_populates="register")

    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=False)
    unit = db.relationship("Unit", back_populates="register")

    @classmethod
    def get_by_units(cls, units):
        return cls.query.filter(cls.unit_id.in_(units)).all()
