from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    from src.models.base import BaseModel
    from src.models.role import Role
    from src.models.unit import Unit
    from src.models.user import User
    from src.models.person import Person
    from src.models.points import Points
    from src.models.meet import Meet
    from src.models.register import Register
    from src.models.check_person import CheckPerson
    from src.models.permission import Permission
    from src.models.revoked_tokens import RevokedToken
