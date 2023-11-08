from flask_restful import Resource

from src.models.user import User
from sqlalchemy import select


class HealthCheckResource(Resource):
    def get(self):
        return "ok", 200


class HealthCheckDatabaseResource(Resource):
    def get(self):
        try:
            # to check database we will execute raw query

            users = select(User)
            print(users)
        except Exception as e:
            output = str(e)
            return output, 400

        return users, 200
