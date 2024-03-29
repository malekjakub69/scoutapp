from marshmallow import Schema, fields
from src.schemas.permission import PermissionSchema
from src.schemas.base import BaseIdSchema


class PersonSchema(BaseIdSchema):
    first_name = fields.String(required=False, allow_none=True)
    last_name = fields.String(required=False, allow_none=True)
    email = fields.Email(required=True)
    mobile = fields.String(required=False, allow_none=True)
    address = fields.String(required=False, allow_none=True)
    birth_date = fields.Date(required=False, allow_none=True)
    nickname = fields.String(required=False, allow_none=True)
    register = fields.List(fields.Nested("RegisterSchema"), dump_only=True)
    user = fields.Nested("UserSchema", dump_only=True)
    # points = fields.List(fields.Nested("PointsSchema"), dump_only=True)
    # check_persons = fields.List(fields.Nested("CheckPersonSchema"), dump_only=True)
