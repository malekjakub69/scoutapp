from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.role import Role
from src.models.troop import Troop
from src.models.user import User
from src.models.member import Member
from src.models.points import Points
from src.models.meet import Meet
from src.models.register import Register
from src.models.check_member import CheckMember
from src.models.permission import Permission
from src.models.revoked_tokens import RevokedToken

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:MyV3ryS3cr3t3Passw0rd@db:5432/ScoutApp"
db = SQLAlchemy(app)


def init_database():
    mainTroop = Troop(name="Main troop", number=0, code="")
    troop = Troop(name="Sestka", number=6, code="0.6", parent_troop=mainTroop)

    userAdmin = User(
        email="admin@sez.cz",
        login="admin",
        password=User.hash_password("Password1"),
        first_name="Admin",
        surname="Scout",
        current_troop=mainTroop,
    )

    userMember = User(
        email="member@sez.cz",
        login="member",
        password=User.hash_password("Password1"),
        first_name="Member",
        surname="Scout",
        current_troop=troop,
    )

    roleAdmin = Role(code="admin", name="Admin")
    roleMember = Role(code="member", name="Member")

    permission1 = Permission(role=roleAdmin, troop=mainTroop, user=userAdmin)
    permission2 = Permission(role=roleMember, troop=troop, user=userMember)

    member1 = Member(first_name="Admin", surname="Scout", email="test@email.cz")

    db.session.add_all(
        [mainTroop, troop, userAdmin, userMember, roleAdmin, roleMember, permission1, permission2, member1]
    )
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        init_database()
