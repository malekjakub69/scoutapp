from marshmallow import Schema, fields

from src.schemas.base import BaseIdSchema


class RoleSchema(BaseIdSchema):
    name = fields.String(required=True, allow_none=False)
    code = fields.String(required=True, allow_none=False)
