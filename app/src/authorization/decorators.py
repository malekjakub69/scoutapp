from functools import wraps
from typing import Any, Callable

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import request
from logger import logger
from src.models.user import User
from src.translations.translator import Translator
from werkzeug.exceptions import NotFound, Unauthorized


def authorize_roles(role_codes: list):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user = User.get_by_email_or_login(get_jwt_identity(), set_language=False)
            logger.bind(user_id=user.id if user else None)
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.is_registered:
                raise Unauthorized(Translator.localize("user_not_registered"))
            request.__setattr__("language", user.resolve_language())
            if user.role.code not in role_codes:
                raise Unauthorized(Translator.localize("unauthorized"))
            return func(*args, **kwargs)

        return wrapped

    return wrapper


def authorize_roles_except(role_codes: list):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user = User.get_by_email_or_login(get_jwt_identity(), set_language=False)
            logger.bind(user_id=user.id if user else None)
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.is_registered:
                raise Unauthorized(Translator.localize("user_not_registered"))
            request.__setattr__("language", user.resolve_language())
            if user.role.code in role_codes:
                raise Unauthorized(Translator.localize("unauthorized"))
            return func(*args, **kwargs)

        return wrapped

    return wrapper


def authorize_all():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        @jwt_required()
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            user = User.get_by_email_or_login(get_jwt_identity(), set_language=False)
            logger.bind(user_id=user.id if user else None)
            if not user:
                raise NotFound("auth: User does not exist!")
            if not user.is_registered:
                raise Unauthorized(Translator.localize("user_not_registered"))
            request.__setattr__("language", user.resolve_language())
            request.__setattr__("current_user", user)
            return func(*args, **kwargs)

        return wrapped

    return wrapper
