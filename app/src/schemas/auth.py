from marshmallow import Schema, fields


class LoginSchema(Schema):
    login = fields.String(required=True, load_only=True)
    password = fields.String(required=True, load_only=True)


class RegistrationSchema(Schema):
    email = fields.String(required=True, load_only=True)
    login = fields.String(required=False, load_only=True)
    new_password = fields.String(required=True, load_only=True)
    new_password_repeat = fields.String(required=True, load_only=True)
