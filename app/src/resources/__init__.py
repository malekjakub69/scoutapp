from src.resources.internal import *


def register_resources(api, version):
    # Internal
    api.add_resource(HealthCheckResource, f"{version}/healthcheck")
    api.add_resource(HealthCheckDatabaseResource, f"{version}/healthcheck_db")
