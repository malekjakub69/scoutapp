from src.resources.test import *
from src.resources.check_member import *
from src.resources.meet import *
from src.resources.auth import *
from src.resources.member import *
from src.resources.permission import *
from src.resources.points import *
from src.resources.register import *
from src.resources.role import *
from src.resources.troop import *
from src.resources.user import *
from src.resources.internal import *


def register_resources(api, version):
    # Internal
    api.add_resource(HealthCheckResource, f"{version}/healthcheck")  # GET
    api.add_resource(HealthCheckDatabaseResource, f"{version}/healthcheck_db")  # GET
    # Auth
    api.add_resource(LoginResource, f"{version}/login")  # POST
    api.add_resource(RegistrationResource, f"{version}/registration")  # POST
    # User
    api.add_resource(UsersResource, f"{version}/users", f"{version}/user/<int:user_id>")  # GET. DELETE
    api.add_resource(UserChangeTroop, f"{version}/change_troop")  # POST
    # Troop
    api.add_resource(TroopResource, f"{version}/troops", f"{version}/troop/<int:troop_id>")  # GET, POST, DELETE
    # Role
    api.add_resource(RoleResource, f"{version}/roles", f"{version}/role/<int:role_id>")  # GET, POST, DELETE
    # Permission
    api.add_resource(PermissionResource, f"{version}/permission")  # POST
    # Test
    api.add_resource(ResetDatabaseResource, f"{version}/reset_db")
    api.add_resource(DatasetResource, f"{version}/import_dataset")  # GET
