from src.models.troop import Troop
from src.resources.base import BaseResource

from src.models.user import User
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound, BadRequest
from src.authorization.decorators import authorize_roles, authorize_all


class UsersResource(BaseResource):
    @authorize_roles(["admin"])
    def get(self):
        users = User.get_items()
        return self.result(serialize("UserSchema", users))

    @authorize_roles(["admin"])
    def delete(self, user_id: int):
        if not (user := User.get_by_id(user_id)):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("message")))
        user.delete()
        return {"user:": Translator.localize("entity_deleted", Translator.localize("troop"), user_id)}


class UserChangeTroop(BaseResource):
    @authorize_all()
    def post(self):
        user = self.current_user
        data = deserialize("UserChangeTroopSchema", request.get_json())
        if not (troop := Troop.get_by_id(data["troop_id"])):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("troop")))
        avaliable_troop_ids = [permission.troop_id for permission in user.permissions]
        if troop.id not in avaliable_troop_ids:
            raise BadRequest(Translator.localize("troop_not_available", troop.name))
        user.current_troop_id = troop.id
        user.save()
        return self.result(serialize("UserSchema", user))
