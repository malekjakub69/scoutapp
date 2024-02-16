from flask_restful import Resource
from src.models.base import Transaction
from src.models.permission import Permission
from src.models.role import Role
from src.models.user import User

from src.models.unit import Unit


class HealthCheckResource(Resource):
    def get(self):
        return {"message": "ok"}, 200


class HealthCheckDatabaseResource(Resource):
    """
    Resource for checking the health of the database.
    Attempts to create a new role, retrieve it, and delete it.
    Returns a success message if the database is working properly.
    """

    def get(self):
        try:
            role = Unit.query.filter_by(code="001.11").first()
            if role == None:
                new_unit = Unit(name="test", number=1, code="001.11")
                new_unit.save()

            role = Unit.query.filter_by(code="001.11").first()

            role.delete()

        except Exception as e:
            output = str(e)
            return output, 400

        return {"message": "Db works"}, 200


class InitDb(Resource):
    def get(self):
        transaction = Transaction()
        transaction.clear_db()
        transaction.commit()

        transaction.create_db()
        transaction.commit()

        user = User(email="admin@skaut.cz", login="admin", password=User.hash_password("Password1"), first_name="Admin", last_name="Skaut")
        role1 = Role(name="Admin", code="admin")
        role2 = Role(name="Leader", code="leader")
        role3 = Role(name="Mentor", code="mentor")
        role4 = Role(name="Person", code="person")
        unit = Unit(name="MainUnit", number=1, code="01")
        permission = Permission(role=role1, unit=unit, user=user)

        transaction.add(user, role1, role2, role3, role4, unit, permission)
        transaction.commit()
