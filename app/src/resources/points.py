import json
from flask_restful import Resource


class PointResource(Resource):
    def get(self):
        return "ok", 200
