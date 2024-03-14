from flask_restful import Resource
from src.models.register import Register
from src.models.person import Person
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

        role1 = Role(name="Admin", code="admin")
        role2 = Role(name="Leader", code="leader")
        role3 = Role(name="Mentor", code="mentor")
        role4 = Role(name="Person", code="person")

        unitZlutaPonorka = Unit(name="Žlutá Ponorka", number=0, code="zlutaPonorka")
        unitPetka = Unit(name="5. oddíl VS Třebíč", number=1, code="petka", parent_unit=unitZlutaPonorka)
        unitCtyrka = Unit(name="4. oddíl VS Třebíč", number=1, code="ctyrka", parent_unit=unitZlutaPonorka)
        unitSestka = Unit(name="6. oddíl VS Třebíč", number=2, code="sestka", parent_unit=unitZlutaPonorka)

        personAdmin = Person(
            first_name="Admin",
            last_name="Skaut",
            nickname="Adminious",
            email="admin@skaut.cz",
            mobile="123456789",
            address="Skautská 1, Třebíč",
            birth_date="2000-01-01",
        )

        personLeader = Person(
            first_name="Leader",
            last_name="Skaut",
            nickname="Adminious",
            email="leader@skaut.cz",
            mobile="123456789",
            address="Skautská Leader, Třebíč",
            birth_date="2000-01-01",
        )

        person1 = Person(
            first_name="Test",
            last_name="Test1",
            nickname="Tests",
            email="test1@skaut.cz",
            mobile="98765432",
            address="Skautská 2, Třebíč",
            birth_date="2000-02-01",
        )

        person2 = Person(
            first_name="Test",
            last_name="Test2",
            nickname="Tests",
            email="test2@skaut.cz",
            mobile="98765432",
            address="Skautská 2, Třebíč",
            birth_date="2000-02-01",
        )
        person3 = Person(
            first_name="John",
            last_name="Doe",
            nickname="JD",
            email="john.doe@example.com",
            mobile="987654321",
            address="123 Main St, Anytown",
            birth_date="1990-05-15",
        )

        person4 = Person(
            first_name="Jane",
            last_name="Smith",
            nickname="JS",
            email="jane.smith@example.com",
            mobile="1234567890",
            address="456 Elm St, Anytown",
            birth_date="1995-10-20",
        )

        userAdmin = User(
            email="admin@skaut.cz",
            login="admin",
            password=User.hash_password("Password1"),
            first_name="Admin",
            last_name="Skaut",
            person=personAdmin,
            current_unit=unitZlutaPonorka,
        )

        userLeader = User(
            email="leader@skaut.cz",
            login="leader",
            password=User.hash_password("Password1"),
            first_name="Leader",
            last_name="Skaut",
            person=person2,
            current_unit=unitPetka,
        )

        registers = [
            Register(person=personAdmin, unit=unitZlutaPonorka),
            Register(person=personLeader, unit=unitPetka),
            Register(person=person2, unit=unitSestka),
            Register(person=person3, unit=unitPetka),
            Register(person=person3, unit=unitSestka),
            Register(person=person4, unit=unitPetka),
        ]
        permissions = [
            Permission(role=role1, unit=unitZlutaPonorka, user=userAdmin),
            Permission(role=role2, unit=unitPetka, user=userLeader),
        ]

        transaction.add(userAdmin, userLeader, role1, role2, role3, role4)

        transaction.add(unitPetka, unitSestka, unitCtyrka, unitZlutaPonorka, personAdmin, personLeader, person2)

        transaction.add(registers, permissions)

        transaction.commit()
