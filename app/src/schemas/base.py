from marshmallow import EXCLUDE, Schema, fields


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class BaseIdSchema(BaseSchema):
    format = "%Y-%m-%dT%H:%M:%S"

    id = fields.Integer(dump_only=True)
    active = fields.Boolean(dump_only=True)

    created_on = fields.DateTime(dump_only=True, format=format)
    updated_on = fields.DateTime(dump_only=True, format=format)
