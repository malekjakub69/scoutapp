from src.resources.check_person import *
from src.resources.meet import *
from src.resources.auth import *
from src.resources.person import *
from src.resources.permission import *
from src.resources.points import *
from src.resources.register import *
from src.resources.role import *
from src.resources.unit import *
from src.resources.user import *
from src.resources.internal import *


def register_resources(api, v):
    # Internal
    api.add_resource(HealthCheckResource, f"{v}/healthcheck")  # GET
    api.add_resource(HealthCheckDatabaseResource, f"{v}/healthcheck_db")  # GET
    api.add_resource(InitDb, f"{v}/init_db")  # GET
    # Auth
    api.add_resource(LoginResource, f"{v}/login")  # POST
    api.add_resource(RegistrationResource, f"{v}/registration")  # POST
    api.add_resource(UserLogoutAccess, f"{v}/logout/access")  # POST
    api.add_resource(UserLogoutRefresh, f"{v}/logout/refresh")  # POST
    api.add_resource(Authenticate, f"{v}/authenticate")  # POST
    # User
    api.add_resource(UsersResource, f"{v}/users")  # GET all
    api.add_resource(UserSelfResource, f"{v}/user")  # GET single
    api.add_resource(UserResource, f"{v}/user/<int:user_id>")  # GET single, POST, DELETE
    api.add_resource(UserChangeUnit, f"{v}/change_unit")  # POST
    # Unit
    api.add_resource(UnitsResource, f"{v}/units")  # GET all
    api.add_resource(UnitResource, f"{v}/unit", f"{v}/unit/<int:unit_id>")  # GET single, POST, DELETE
    # Role
    api.add_resource(RolesResource, f"{v}/roles")  # GET all
    api.add_resource(RoleResource, f"{v}/role", f"{v}/role/<int:role_id>")  # GET single, POST, DELETE
    # Permission
    api.add_resource(PermissionResource, f"{v}/permission")  # POST
    # Person
    api.add_resource(PersonsResource, f"{v}/persons")  # GET all
    api.add_resource(PersonResource, f"{v}/person", f"{v}/person/<int:person_id>")  # GET single, POST, DELETE
    # CheckPerson
    api.add_resource(CheckPersonsResource, f"{v}/check_persons")  # GET all
    api.add_resource(CheckPersonResource, f"{v}/check_person", f"{v}/check_person/<int:check_person_id>")  #  GET single, POST, DELETE
    api.add_resource(CheckPersonByHashResource, f"{v}/check_person/<string:person_hash>")  # GET single
    # Meet
    api.add_resource(MeetsResource, f"{v}/meets")  # GET all
    api.add_resource(MeetResource, f"{v}/meet", f"{v}/meet/<int:meet_id>")  # GET single, POST, DELETE
    # Points
    api.add_resource(PointsResource, f"{v}/points")  # GET all
    api.add_resource(PointResource, f"{v}/point", f"{v}/point/<int:point_id>")  # GET single, POST, DELETE
