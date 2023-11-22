from src.models.troop import Troop
from src.models.role import Role
from src.models.user import User
from src.models import db
from src.translations.translator import Translator
from src.resources.base import BaseResource


class ResetDatabaseResource(BaseResource):
    def get(self):
        db.reflect()
        db.drop_all()
        return {Translator.localize("all tables drops")}


class DatasetResource(BaseResource):
    userAdmin = User(
        email="admin@sez.cz",
        login="admin",
        password=User.hash_password("Password1"),
        first_name="Admin",
        surname="Scout",
    )
    userMember = User(
        email="member@sez.cz",
        login="member",
        password=User.hash_password("Password1"),
        first_name="Member",
        surname="Scout",
    )

    mainTroop = Troop(name="Main troop", number=0, code="0")
    troop = Troop(name="Sestka", number=6, code="0.6")

    roleAdmin = Role(code="admin", name="Admin")
    roleMember = Role(code="member", name="Member")

    def get(self):
        self.userAdmin.save()
        self.userMember.save()
        self.mainTroop.save()
        self.troop.save()
        self.roleAdmin.save()
        self.roleMember.save()
