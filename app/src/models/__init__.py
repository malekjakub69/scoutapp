from sqlalchemy import create_engine


def init_db():
    from src.models.base import BaseModel
    from src.models.role import Role
    from src.models.troop import Troop
    from src.models.user import User
    from src.models.member import Member
    from src.models.points import Points
    from src.models.meet import Meet
    from src.models.register import Register
    from src.models.check_member import CheckMember

    # Nastavení databáze
    return BaseModel.metadata
