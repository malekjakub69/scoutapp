import datetime
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from src.models.revoked_tokens import RevokedToken
from src.translations.translator import Translator
from src.models.user import User
from src.schemas import deserialize, serialize
from werkzeug.exceptions import BadRequest, Conflict, Unauthorized
from src.authorization import jwt


class LoginResource(Resource):
    @jwt_required(optional=True)
    def post(self):
        logged_user = get_jwt_identity()
        if logged_user:
            return {"message": f"Already logged in as {logged_user}"}

        data = deserialize("LoginSchema", request.get_json())
        current_user = User.get_by_email_or_login(data["login"])

        if not current_user:
            raise Unauthorized(Translator.localize("wrong_username"))
        if not current_user.active:
            return {"message": Translator.localize("user_not_active")}, 202
        if User.verify_password(current_user.password, data["password"]):
            access_token = create_access_token(identity=current_user.email)
            refresh_token = create_refresh_token(identity=current_user.email)

            current_user.last_login = datetime.datetime.now()
            current_user.save()

            return {
                "item": serialize("UserSchema", current_user),
                "message": f"Logged in as {current_user.first_name} {current_user.last_name}",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        else:
            raise Unauthorized(Translator.localize("wrong_password"))


class RegistrationResource(Resource):
    def post(self):
        data = deserialize("RegistrationSchema", request.get_json(), partial=True)
        user = User.get_by_email_or_login(data["email"])
        if user:
            raise Conflict(Translator.localize("user_already_registered", user.email))
        user = User.get_by_email_or_login(data["login"])
        if user:
            raise Conflict(Translator.localize("user_already_registered", user.email))
        if not data["email"]:
            raise BadRequest(Translator.localize("email_required"))
        if not data["new_password"] or not data["new_password_repeat"]:
            raise BadRequest(Translator.localize("password_required"))
        if data["new_password"] != data["new_password_repeat"]:
            raise BadRequest(Translator.localize("wrong_new_password"))

        user = User()
        user.password = User.hash_password(data["new_password"])
        user.login = data["login"] if "login" in data else None
        user.email = data["email"]
        user.active = True
        user.last_login = datetime.datetime.now()
        user.save()

        access_token = create_access_token(identity=data["email"].lower())
        refresh_token = create_refresh_token(identity=data["email"].lower())

        return (
            {
                "message": Translator.localize("user_registered", f"{user.first_name} {user.last_name}"),
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            201,
        )


class Authenticate(Resource):
    @jwt_required()
    def post(self):
        # Returns current user if token is valid. Otherwise a client error is returned.
        current_user = User.get_by_email_or_login(get_jwt_identity())
        if current_user:
            return serialize("UserSchemaExtended", current_user)
        raise Unauthorized(Translator.localize("entity_not_found", Translator.localize("user")))


class UserLogoutAccess(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        revoked_token = RevokedToken(jti=jti)
        revoked_token.save()
        return {"message": "Access token has been revoked"}


class UserLogoutRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        jti = get_jwt()["jti"]
        revoked_token = RevokedToken(jti=jti)
        revoked_token.save()
        return {"message": "Refresh token has been revoked"}


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return RevokedToken.is_jti_blocklisted(jti)
