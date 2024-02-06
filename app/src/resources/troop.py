from src.models.permission import Permission
from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.troop import Troop
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all, authorize_roles
from src.translations.translator import Translator


class TroopsResource(BaseResource):
    @authorize_all()
    def get(self):
        troops = Troop.get_items()
        return self.result(serialize("TroopSchema", troops))


class TroopResource(BaseResource):
    @authorize_all()
    def get(self, troop_id: int):
        troop = Troop.get_by_id(troop_id)
        return self.result(serialize("TroopSchema", troop))

    @authorize_all()
    def post(self):
        data = deserialize("TroopSchema", request.get_json())
        exist_troop = Troop.get_by_code(data["code"])
        if exist_troop:
            raise Conflict(Translator.localize("troop_exist"))

        if not (parent_troop := Troop.get_by_id(data["parent_troop_id"])):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("parent_troop")))

        transaction = Transaction()
        troop = Troop(**data)
        transaction.add(troop)
        transaction.commit()

        permissions = parent_troop.permissions

        new_permissions = []
        for permission in permissions:
            new_permissions.append(Permission(role_id=permission.role_id, troop=troop, user_id=permission.user_id))

        transaction.merge(*new_permissions)
        transaction.commit()

        return (self.result(serialize("TroopSchema", troop)), 201)

    @authorize_all()
    def delete(self, troop_id: int):
        if not (troop := Troop.get_by_id(troop_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        troop.delete()
        return {"troop": Translator.localize("entity_deleted", troop_id)}
