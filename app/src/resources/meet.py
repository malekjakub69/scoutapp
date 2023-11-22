import json
from flask_restful import Resource


class MeetResource(Resource):
    def get(self):
        return "ok", 200
