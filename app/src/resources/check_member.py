import json
from flask_restful import Resource


class CheckMemberResource(Resource):
    def get(self):
        return "ok", 200
