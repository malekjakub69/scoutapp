from marshmallow import fields

from src.schemas.base import BaseIdSchema


class PermissionSchema(BaseIdSchema):
    troop_id = fields.Integer(required=True, allow_none=False)
    role_id = fields.Integer(required=True, allow_none=False)


class PermissionsSchema(BaseIdSchema):
    permissions = fields.List(fields.Nested(PermissionSchema), required=True, allow_none=False)
    user_id = fields.Integer(required=True, allow_none=True)
