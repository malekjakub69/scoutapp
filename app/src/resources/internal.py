from flask_restful import Resource

from src.models.user import User
from src.models import db


class HealthCheckResource(Resource):
    def get(self):
        return "ok", 200


class HealthCheckDatabaseResource(Resource):
    def get(self):
        try:
            # to check database we will execute raw query
            User.get_by_email_or_login("admin")
        except Exception as e:
            output = str(e)
            return output, 400

        return "database is ok", 200
