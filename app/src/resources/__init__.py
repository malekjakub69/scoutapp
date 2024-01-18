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


def register_resources(api, v):
    # Internal
    api.add_resource(HealthCheckResource, f"{v}/healthcheck")  # GET
    api.add_resource(HealthCheckDatabaseResource, f"{v}/healthcheck_db")  # GET
    # Auth
    api.add_resource(LoginResource, f"{v}/login")  # POST
    api.add_resource(RegistrationResource, f"{v}/registration")  # POST
    # User
    api.add_resource(UsersResource, f"{v}/users")  # GET all
    api.add_resource(UserResource, f"{v}/user" f"{v}/user/<int:user_id>")  # GET single, POST, DELETE
    api.add_resource(UserChangeTroop, f"{v}/change_troop")  # POST
    # Troop
    api.add_resource(TroopsResource, f"{v}/troops")  # GET all
    api.add_resource(TroopResource, f"{v}/troop", f"{v}/troop/<int:troop_id>")  # GET single, POST, DELETE
    # Role
    api.add_resource(RolesResource, f"{v}/roles")  # GET all
    api.add_resource(RoleResource, f"{v}/role", f"{v}/role/<int:role_id>")  # GET single, POST, DELETE
    # Permission
    api.add_resource(PermissionResource, f"{v}/permission")  # POST
    # Member
    api.add_resource(MembersResource, f"{v}/members")  # GET all
    api.add_resource(MemberResource, f"{v}/member", f"{v}/member/<int:member_id>")  # GET single, POST, DELETE
    # CheckMember
    api.add_resource(CheckMembersResource, f"{v}/check_members")  # GET all
    api.add_resource(CheckMemberResource, f"{v}/check_member", f"{v}/check_member/<int:check_member_id>")  #  GET single, POST, DELETE
    api.add_resource(CheckMemberByHashResource, f"{v}/check_member/<string:member_hash>")  # GET single
    # Meet
    api.add_resource(MeetsResource, f"{v}/meets")  # GET all
    api.add_resource(MeetResource, f"{v}/meet", f"{v}/meet/<int:meet_id>")  # GET single, POST, DELETE
    # Points
    api.add_resource(PointsResource, f"{v}/points")  # GET all
    api.add_resource(PointResource, f"{v}/point", f"{v}/point/<int:point_id>")  # GET single, POST, DELETE
