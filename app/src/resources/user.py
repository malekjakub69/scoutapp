from flask_jwt_extended import get_jwt_identity, jwt_required
from src.models.base import Transaction
from src.models.troop import Troop
from src.resources.base import BaseResource

from src.models.user import User
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, Unauthorized
from src.authorization.decorators import authorize_roles, authorize_all


class UsersResource(BaseResource):
    @authorize_all()
    def get(self):
        users = User.get_items()
        return self.result(serialize("UserSchema", users))


class IdentityResource(BaseResource):
    @authorize_all()
    def get(self):
        user = User.get_by_email_or_login(get_jwt_identity())
        return self.result(serialize("UserSchema", user))


class UserSelfResource(BaseResource):
    @jwt_required()
    def get(self):
        user = User.get_by_email_or_login(get_jwt_identity())
        return self.resultSingle(serialize("UserSchema", user))


class UserResource(BaseResource):
    @authorize_all()
    def get(self, user_id: int):
        user = User.get_by_id(user_id)
        return self.result(serialize("UserSchema", user))

    @authorize_all()
    def post(self):
        data = deserialize("TroopSchema", request.get_json())
        exist_troop = Troop.get_by_code(data["code"])
        if exist_troop:
            raise Conflict(Translator.localize("troop_exist"))
        transaction = Transaction()
        troop = Troop(**data)
        transaction.add(troop)
        transaction.commit()

        return (self.result(serialize("UserSchema", troop)), 201)

    @authorize_all()
    def delete(self, user_id: int):
        if not (user := User.get_by_id(user_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        user.delete()
        return {"user:": Translator.localize("entity_deleted", user_id)}


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
