from flask_jwt_extended import jwt_required
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.points import Points
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class PointsResource(BaseResource):
    @authorize_all()
    def get(self):
        points = Points.get_items()
        return self.result(serialize("PointsSchema", points))


class PointResource(BaseResource):
    @jwt_required()
    def get(self, point_id: int):
        point = Points.get_by_id(point_id)
        return self.result(serialize("PointsSchema", point))

    @jwt_required()
    def post(self):
        data = deserialize("PointsSchema", request.get_json())
        transaction = Transaction()
        point = Points(**data)
        transaction.add(point)
        transaction.commit()

        return (self.result(serialize("PointsSchema", point)), 201)

    @jwt_required()
    def delete(self, point_id: int):
        if not (point := Points.get_by_id(point_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        point.delete()
        return {"point:": Translator.localize("entity_deleted", point_id)}
