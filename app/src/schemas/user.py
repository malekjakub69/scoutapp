from marshmallow import Schema, fields
from src.schemas.permission import PermissionSchema
from src.schemas.base import BaseIdSchema


class UserSchema(BaseIdSchema):
    first_name = fields.String(required=False, allow_none=True)
    last_name = fields.String(required=False, allow_none=True)
    login = fields.String(required=False, allow_none=True)
    email = fields.Email(required=True)
    last_login = fields.DateTime(required=True, dump_only=True)
    current_troop_id = fields.Integer(required=False, allow_none=True)
    permission = fields.List(fields.Nested(PermissionSchema), dump_only=True)


class UserChangeTroopSchema(Schema):
    troop_id = fields.Integer(required=True, allow_none=False)
