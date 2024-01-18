from flask_jwt_extended import jwt_required
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.meet import Meet
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class MeetsResource(BaseResource):
    @authorize_all()
    def get(self):
        meet = Meet.get_items()
        return self.result(serialize("MeetSchema", meet))


class MeetResource(BaseResource):
    @jwt_required()
    def get(self, meet_id: int):
        meet = Meet.get_by_id(meet_id)
        return self.result(serialize("MeetSchema", meet))

    @jwt_required()
    def post(self):
        data = deserialize("MeetSchema", request.get_json())
        transaction = Transaction()
        meet = Meet(**data)
        transaction.add(meet)
        transaction.commit()

        return (self.result(serialize("MeetSchema", meet)), 201)

    @jwt_required()
    def delete(self, meet_id: int):
        if not (meet := Meet.get_by_id(meet_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        meet.delete()
        return {"meet:": Translator.localize("entity_deleted", meet_id)}
