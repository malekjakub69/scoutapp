from src.models import db
from src.models.base import BaseIdModel


class Unit(BaseIdModel):
    """
    Represents a unit in the ScoutApp system.

    Attributes:
        name (str): The name of the unit.
        number (int): The number of the unit.
        code (str): The unique code of the unit.
        units (list[Unit]): The child units of this unit.
        parent_unit (Unit): The parent unit of this unit.
        parent_unit_id (int): The ID of the parent unit, if any.
        users (list[User]): The users currently assigned to this unit.
        roles (list[Role]): The roles assigned to this unit.
        register (list[Register]): The registers associated with this unit.
        meets (list[Meet]): The meets associated with this unit.
    """

    __tablename__ = "unit"

    name = db.Column(db.String(120), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    code = db.Column(db.String(16), nullable=False, unique=True)

    # self 1:N
    ## Unit hierarchy
    parent_unit_id = db.Column(db.Integer(), db.ForeignKey("unit.id"), nullable=True)
    parent_unit = db.relationship("Unit", back_populates="units", uselist=False, remote_side="Unit.id")
    units = db.relationship("Unit", back_populates="parent_unit")

    # 1:N
    ## Current unit
    users = db.relationship("User", back_populates="current_unit")
    ## Role in unit
    permissions = db.relationship("Permission", back_populates="unit")
    ## Register in unit
    register = db.relationship("Register", back_populates="unit")

    meets = db.relationship("Meet", back_populates="unit")

    @classmethod
    def get_subtree(cls, unit_id):

        def _get_subtree_recursive(unit_id):
            child_units = cls.query.filter_by(parent_unit_id=unit_id).all()
            subtree = []
            for child_unit in child_units:
                subtree.append(child_unit)
                subtree.extend(_get_subtree_recursive(child_unit.id))
            return subtree

        return _get_subtree_recursive(unit_id)
