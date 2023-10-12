from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    from src.models.role import Role
    from src.models.troop import Troop
    from src.models.user import User
