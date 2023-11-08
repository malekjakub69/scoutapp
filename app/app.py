import os
from flask import Flask
from flask_restful import Api

from middleware import after_request, before_request

env_to_config_file = {"dev": "dev_config.cfg", "prod": "prod_config.cfg"}


def create_app():
    # configure logger

    # create application
    app = Flask(__name__, template_folder=os.path.join("src", "templates"))
    config_file = env_to_config_file.get(os.environ.get("CONFIGURATION", "dev"))
    app.config.from_pyfile(f"configurations/{config_file}")

    app.before_request(before_request)
    app.after_request(after_request)

    # create API
    api = Api(app)

    from src.resources import register_resources

    register_resources(api, "/v1")

    return app


# init database
# from src.models import db, init_db


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
