from marshmallow import fields

from src.schemas.base import BaseIdSchema


class CheckPersonSchema(BaseIdSchema):
    person_hash = fields.Integer(required=True, allow_none=False)
    other_desc = fields.Integer(required=True, allow_none=False)
    confirm = fields.Boolean(required=True, allow_none=False)
    no_reason = fields.String(required=True, allow_none=False)
    sent = fields.Boolean(required=True, allow_none=False)
    person = fields.Nested("PersonSchema", required=True, allow_none=False)
    meet = fields.Nested("MeetSchema", required=True, allow_none=False)


class CheckPersonConfirmSchema(BaseIdSchema):
    confirm = fields.Boolean(required=True, allow_none=False)
    no_reason = fields.String(required=True, allow_none=False)
    other_desc = fields.String(required=True, allow_none=False)
