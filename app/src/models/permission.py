from src.models import db
from src.models.base import BaseIdModel


class Permission(BaseIdModel):
    """
    Represents a permission granted to a user for a specific role and unit.

    Attributes:

        user_id (int): The ID of the user associated with the permission.
        user (User): The user associated with the permission.
        role_id (int): The ID of the role associated with the permission.
        role (Role): The role associated with the permission.
        unit_id (int): The ID of the unit associated with the permission.
        unit (Unit): The unit associated with the permission.
    """

    __tablename__ = "permission"

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    role = db.relationship("Role", back_populates="permissions", uselist=False)

    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=False)
    unit = db.relationship("Unit", back_populates="permissions", uselist=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="permissions", uselist=False)

    @classmethod
    def get_item(cls, _user_id, _unit_id):
        return cls.query.filter_by(user_id=_user_id, unit_id=_unit_id).first()

    @classmethod
    def get_item_by_user_id(self, _user_id):
        return self.query.filter_by(user_id=_user_id).all()
