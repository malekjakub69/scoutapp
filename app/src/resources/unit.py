from flask_jwt_extended import get_jwt_identity
from src.models.role import Role
from src.models.user import User
from src.models.permission import Permission
from src.resources.base import BaseResource
from src.models.base import Transaction
from src.models.unit import Unit
from flask_restful import request
from src.schemas import deserialize, serialize
from werkzeug.exceptions import NotFound, Conflict

from src.authorization.decorators import authorize_all, authorize_roles
from src.translations.translator import Translator


class UnitsResource(BaseResource):
    @authorize_all()
    def get(self):
        units = Unit.get_items()
        return self.result(serialize("UnitSchema", units))


class UnitResource(BaseResource):
    @authorize_all()
    def get(self, unit_id: int):
        unit = Unit.get_by_id(unit_id)
        return self.result(serialize("UnitSchema", unit))

    @authorize_all()
    def post(self):
        data = deserialize("UnitSchema", request.get_json())
        exist_unit = Unit.get_by_code(data["code"])
        if exist_unit:
            raise Conflict(Translator.localize("unit_exist"))

        if not (parent_unit := Unit.get_by_id(data["parent_unit_id"])):
            raise NotFound(Translator.localize("entity_not_found", Translator.localize("parent_unit")))

        # Create new unit
        transaction = Transaction()
        unit = Unit(**data)
        transaction.add(unit)
        transaction.commit()

        # Add permissions to the new unit from the parent unit
        permissions = parent_unit.permissions

        new_permissions = []
        for permission in permissions:
            new_permissions.append(Permission(role_id=permission.role_id, unit=unit, user_id=permission.user_id))

        # Add admin permissions to the user who created the unit
        new_permissions.append(Permission(role_id=Role.get_by_code("admin").id, unit=unit, user=User.get_by_email_or_login(get_jwt_identity())))

        transaction.merge(*new_permissions)
        transaction.commit()

        return (self.result(serialize("UnitSchema", unit)), 201)

    @authorize_all()
    def delete(self, unit_id: int):
        if not (unit := Unit.get_by_id(unit_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        unit.delete()
        return {"unit": Translator.localize("entity_deleted", unit_id)}
