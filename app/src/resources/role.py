from logger import logger
from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.role import Role
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all, authorize_roles
from src.translations.translator import Translator


class RoleResource(BaseResource):
    @authorize_all()
    def get(self):
        troops = Role.get_items()
        return self.result(serialize("RoleSchema", troops))

    @authorize_all()
    def post(self):
        data = deserialize("RoleSchema", request.get_json())
        exist_role = Role.get_by_code(data["code"])
        if exist_role:
            logger.warning(f"Role code {data['code']} already exist.")
            raise Conflict(Translator.localize("role_exist"))
        transaction = Transaction()
        role = Role(**data)
        transaction.add(role)
        transaction.commit()

        # self.emit_websocket_notification("new-message", {"message_id": message.id, "user_id": message.user_id})

        return (
            self.result(
                serialize("RoleSchema", role),
                Translator.localize("entity_created", Translator.localize("message"), ""),
            ),
            201,
        )

    @authorize_all()
    def delete(self, role_id: int):
        if not (troop := Role.get_by_id(role_id)):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("message")))
        troop.delete()
        return {"role": Translator.localize("entity_deleted", Translator.localize("troop"), role_id)}
