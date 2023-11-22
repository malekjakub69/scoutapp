from marshmallow import Schema, fields

from src.schemas.base import BaseIdSchema


class PermissionSchema(BaseIdSchema):
    troop_id = fields.Integer(required=True, allow_none=False)
    role_id = fields.Integer(required=True, allow_none=False)
    user_id = fields.Integer(required=True, allow_none=False)
