from marshmallow import fields

from src.schemas.base import BaseIdSchema


class RegisterSchema(BaseIdSchema):
    unit = fields.Nested("UnitSchema")


class RegistersSchema(BaseIdSchema):
    registers = fields.List(fields.Nested(RegisterSchema), required=True, allow_none=False)
    member_id = fields.Integer(required=True, allow_none=True)
