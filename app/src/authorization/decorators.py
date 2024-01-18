from functools import wraps
from typing import Any, Callable

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import request
from werkzeug.exceptions import NotFound, Unauthorized

from src.models.user import User
from src.translations.translator import Translator


def authorize_roles(role_codes: list):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user: User = User.get_by_email_or_login(get_jwt_identity())
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.active:
                raise Unauthorized(Translator.localize("user_not_active"))
            if user.permissions:
                troop_permissions = [permission for permission in user.permissions if permission.troop_id == user.current_troop_id]
                if not troop_permissions or troop_permissions[0].role.code not in role_codes:
                    raise Unauthorized(Translator.localize("unauthorized"))
            else:
                raise Unauthorized(Translator.localize("unauthorized"))
            return func(*args, **kwargs)

        return wrapped

    return wrapper


def authorize_roles_except(role_codes: list):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user: User = User.get_by_email_or_login(get_jwt_identity())
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.active:
                raise Unauthorized(Translator.localize("user_not_active"))
            if user.permissions.filter_by(troop_id=user.current_troop_id)[0].role.code in role_codes:
                raise Unauthorized(Translator.localize("unauthorized"))
            return func(*args, **kwargs)

        return wrapped

    return wrapper


def authorize_all():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user: User = User.get_by_email_or_login(get_jwt_identity())
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.active:
                raise Unauthorized(Translator.localize("user_not_active"))
            request.__setattr__("current_user", user)
            return func(*args, **kwargs)

        return wrapped

    return wrapper
