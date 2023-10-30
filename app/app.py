import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException

from logger import logger

env_to_config_file = {"dev": "dev_config.cfg", "prod": "prod_config.cfg"}
from middleware import after_request, before_request


def create_app():
    # configure logger
    logger.configure("eKanban")

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

    app.before_request(before_request)
    app.after_request(after_request)

    _ = Migrate(app, db, compare_type=True)

    # init other extensions
    _ = CORS(app)
    _ = Marshmallow(app)

    from src.authorization import jwt

    jwt.init_app(app)

    from src.resources import register_resources

    register_resources(api, "/v1")

    @app.errorhandler(Exception)
    def handle_error(e):
        status_code = 500
        error = "Something went wrong!"
        if isinstance(e, HTTPException):
            status_code = e.code
            error = e.description
        if status_code >= 500:
            logger.bind(exc_info=e)
        return jsonify(error=error), status_code

    return app


# init database
# from src.models import db, init_db


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
