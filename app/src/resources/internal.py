import json
from flask_restful import Resource

from src.models.troop import Troop


class HealthCheckResource(Resource):
    def get(self):
        return "ok", 200


class HealthCheckDatabaseResource(Resource):
    """
    Resource for checking the health of the database.
    Attempts to create a new role, retrieve it, and delete it.
    Returns a success message if the database is working properly.
    """

    def get(self):
        try:
            role = Troop.query.filter_by(code="001.11").first()
            if role == None:
                new_troop = Troop(name="test", number=1, code="001.11")
                new_troop.save()

            role = Troop.query.filter_by(code="001.11").first()

            role.delete()

        except Exception as e:
            output = str(e)
            return output, 400

        return json.dumps("Db works"), 200
