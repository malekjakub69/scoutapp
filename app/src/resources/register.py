import json
from flask_restful import Resource


class RegisterResource(Resource):
    def get(self):
        return "ok", 200
