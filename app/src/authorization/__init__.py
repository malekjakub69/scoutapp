from flask_jwt_extended import JWTManager

from .decorators import authorize_all, authorize_roles, authorize_roles_except

# init JWT manager
jwt = JWTManager()

__all__ = ["authorize_all", "authorize_roles", "authorize_roles_except"]
