from marshmallow import fields

from src.schemas.base import BaseIdSchema


class UnitSchema(BaseIdSchema):
    name = fields.String(required=True, allow_none=False)
    number = fields.Integer(required=True, allow_none=False)
    code = fields.String(required=True, allow_none=False)
    parent_unit_id = fields.Integer(required=True, allow_none=True)
