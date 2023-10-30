import os
from flask import Flask
from flask_restful import Api

env_to_config_file = {"dev": "dev_config.cfg", "prod": "prod_config.cfg"}


def create_app():
    # configure logger

    # create application
    app = Flask(__name__, template_folder=os.path.join("src", "templates"))
    config_file = env_to_config_file.get(os.environ.get("CONFIGURATION", "dev"))
    app.config.from_pyfile(f"configurations/{config_file}")

    # create API
    api = Api(app)

    # init database
    from src.models import db, init_db

    db.init_app(app)
    init_db()

    from src.resources import register_resources

    register_resources(api, "/v1")

    return app


# init database
# from src.models import db, init_db


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
