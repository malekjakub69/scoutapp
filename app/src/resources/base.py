from typing import Optional
from flask_restful import Resource, request

from src.models.user import User


class BaseResource(Resource):
    def result(self, data: list, message=None) -> dict:
        if data and "items" in data[0]:
            data = data.pop(0)
            result = {}
            for key, value in data.items():
                result[key] = value
        else:
            result = {"items": data}
        result["message"] = message
        return result

    def resultSingle(self, data, message=None) -> dict:
        result = {}
        result["item"] = data
        result["message"] = message
        return result

    @property
    def current_user(self) -> Optional[User]:
        return getattr(request, "current_user", None)
