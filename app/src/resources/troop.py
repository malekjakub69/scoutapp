from logger import logger
from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.troop import Troop
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all, authorize_roles
from src.translations.translator import Translator


class TroopResource(BaseResource):
    @authorize_all()
    def get(self):
        troops = Troop.get_items()
        return self.result(serialize("TroopSchema", troops))

    @authorize_roles(["admin"])
    def post(self):
        data = deserialize("TroopSchema", request.get_json())
        exist_troop = Troop.get_by_code(data["code"])
        if exist_troop:
            logger.warning(f"Troop with code {data['code']} has already been exist.")
            raise Conflict(Translator.localize("troop_exist"))
        transaction = Transaction()
        troop = Troop(**data)
        transaction.add(troop)
        transaction.commit()

        # self.emit_websocket_notification("new-message", {"message_id": message.id, "user_id": message.user_id})

        return (
            self.result(
                serialize("TroopSchema", troop),
                Translator.localize("entity_created", Translator.localize("message"), ""),
            ),
            201,
        )

    @authorize_roles(["admin"])
    def delete(self, troop_id: int):
        if not (troop := Troop.get_by_id(troop_id)):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("message")))
        troop.delete()
        return {"troop": Translator.localize("entity_deleted", Translator.localize("troop"), troop_id)}
