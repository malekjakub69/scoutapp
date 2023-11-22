import json
from flask_restful import Resource


class MemberResource(Resource):
    def get(self):
        return "ok", 200
