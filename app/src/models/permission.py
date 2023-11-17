from src.models import db
from src.models.base import BaseIdModel, BaseTimeModel


class Permission(BaseIdModel, BaseTimeModel):
    """
    Represents a permission granted to a user for a specific role and troop.

    Attributes:

        user_id (int): The ID of the user associated with the permission.
        user (User): The user associated with the permission.
        role_id (int): The ID of the role associated with the permission.
        role (Role): The role associated with the permission.
        troop_id (int): The ID of the troop associated with the permission.
        troop (Troop): The troop associated with the permission.
    """

    __tablename__ = "permission"

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    role = db.relationship("Role", backref="permissions", uselist=False)

    troop_id = db.Column(db.Integer, db.ForeignKey("troop.id"), nullable=False)
    troop = db.relationship("Troop", backref="permissions", uselist=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref="permissions", uselist=False)
