from flask_jwt_extended import get_jwt_identity
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
    @authorize_all()
    def post(self):
        data = deserialize("PermissionsSchema", request.get_json())
        logged_user: User = User.get_by_email_or_login(get_jwt_identity())

        if logged_user.id == data["user_id"]:
            raise Conflict(Translator.localize("permission_denied"))

        transaction = Transaction()

        exist_permission = Permission.get_item_by_user_id(data["user_id"])
        transaction.remove(*exist_permission)

        permissions = []

        for permission in data["permissions"]:
            if not (Role.get_by_id(permission["role_id"])):
                raise NotFound(Translator.localize("entity_not_found", Translator.localize("role")))

            if not (troop := Troop.get_by_id(permission["troop_id"])):
                raise NotFound(Translator.localize("entity_not_found", Translator.localize("troop")))

            permissions.append(Permission(**permission, user_id=data["user_id"]))

            subordinates_troops = Troop.get_subtree(troop.id)

            for subordinate_troop in subordinates_troops:
                subordinate_troop.id
                permissions.append(Permission(role_id=permission["role_id"], troop_id=subordinate_troop.id, user_id=data["user_id"]))

        new_permissions = set(permissions)

        transaction.merge(*list(new_permissions))
        transaction.commit()

        return (self.result(serialize("PermissionSchema", permissions)), 201)
