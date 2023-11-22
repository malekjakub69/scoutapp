from src.models import db
from src.models.base import BaseIdModel


class Role(BaseIdModel):
    """
    Represents a role that a user can have in the system, such as a troop leader or administrator.

    Attributes:
        name (str): The name of the role.
        code (str): The code of the role.
    """

    __tablename__ = "role"

    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(120), unique=True, nullable=False)

    permissions = db.relationship("Permission", back_populates="role")
