from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.role import Role
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all
from src.translations.translator import Translator


class RolesResource(BaseResource):
    @authorize_all()
    def get(self):
        roles = Role.get_items()
        return self.result(serialize("RoleSchema", roles))


class RoleResource(BaseResource):
    @authorize_all()
    def get(self, role_id: int):
        troop = Role.get_by_id(role_id)
        return self.result(serialize("RoleSchema", troop))

    @authorize_all()
    def post(self):
        data = deserialize("RoleSchema", request.get_json())
        exist_role = Role.get_by_code(data["code"])
        if exist_role:
            raise Conflict(Translator.localize("role_exist"))
        transaction = Transaction()
        role = Role(**data)
        transaction.add(role)
        transaction.commit()

        return (self.result(serialize("RoleSchema", role)), 201)

    @authorize_all()
    def delete(self, role_id: int):
        if not (troop := Role.get_by_id(role_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        troop.delete()
        return {"role": Translator.localize("entity_deleted", role_id)}
