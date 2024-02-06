from src.models import db
from src.models.base import BaseIdModel


class Troop(BaseIdModel):
    """
    Represents a troop in the ScoutApp system.

    Attributes:
        name (str): The name of the troop.
        number (int): The number of the troop.
        code (str): The unique code of the troop.
        troops (list[Troop]): The child troops of this troop.
        parent_troop (Troop): The parent troop of this troop.
        parent_troop_id (int): The ID of the parent troop, if any.
        users (list[User]): The users currently assigned to this troop.
        roles (list[Role]): The roles assigned to this troop.
        register (list[Register]): The registers associated with this troop.
        meets (list[Meet]): The meets associated with this troop.
    """

    __tablename__ = "troop"

    name = db.Column(db.String(120), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    code = db.Column(db.String(16), nullable=False, unique=True)

    # self 1:N
    ## Troop hierarchy
    parent_troop_id = db.Column(db.Integer(), db.ForeignKey("troop.id"), nullable=True)
    parent_troop = db.relationship("Troop", back_populates="troops", uselist=False, remote_side="Troop.id")
    troops = db.relationship("Troop", back_populates="parent_troop")

    # 1:N
    ## Current troop
    users = db.relationship("User", back_populates="current_troop")
    ## Role in troop
    permissions = db.relationship("Permission", back_populates="troop")
    ## Register in troop
    register = db.relationship("Register", back_populates="troop")

    meets = db.relationship("Meet", back_populates="troop")

    @classmethod
    def get_subtree(cls, troop_id):

        def _get_subtree_recursive(troop_id):
            child_troops = cls.query.filter_by(parent_troop_id=troop_id).all()
            subtree = []
            for child_troop in child_troops:
                subtree.append(child_troop)
                subtree.extend(_get_subtree_recursive(child_troop.id))
            return subtree

        return _get_subtree_recursive(troop_id)
