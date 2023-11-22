from flask_jwt_extended import get_jwt_identity
from logger import logger
from src.models.role import Role
from src.models.troop import Troop
from src.models.user import User
from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.permission import Permission
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all, authorize_roles
from src.translations.translator import Translator


class PermissionResource(BaseResource):
    @authorize_roles(["admin"])
    def post(self):
        data = deserialize("PermissionSchema", request.get_json())
        logged_user: User = User.get_by_email_or_login(get_jwt_identity())
        role = Role.get_by_id(data["role_id"])
        if not role:
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("role")))
        troop = Troop.get_by_id(data["troop_id"])
        if not troop:
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("troop")))
        if logged_user.current_troop_id == data["troop_id"] and logged_user.id == data["user_id"]:
            raise Conflict(Translator.localize("permission_denied"))
        exist_permission = Permission.get_item(data["user_id"], data["troop_id"], data["role_id"])
        if exist_permission:
            logger.warning(
                f"This permission with this combination already exist. {data['user_id']} {data['troop_id']} {data['role_id']}"
            )
            raise Conflict(Translator.localize("permission_exist"))
        transaction = Transaction()
        permission = Permission(**data)
        transaction.add(permission)
        transaction.commit()

        # self.emit_websocket_notification("new-message", {"message_id": message.id, "user_id": message.user_id})

        return (
            self.result(
                serialize("PermissionSchema", permission),
                Translator.localize("entity_created", Translator.localize("message")),
            ),
            201,
        )
