from typing import Optional

import requests
from flask import current_app
from flask_restful import Resource, request
from werkzeug.exceptions import BadRequest

from logger import logger
from src.models.base import BaseModel
from src.models.user import User
from src.translations.translator import Translator


class BaseResource(Resource):
    supported_params = [("filter", str), ("sort", str), ("page", int), ("limit", int)]
    output_types = {"basic", "default", "extended"}

    def __init__(self):
        super().__init__()

    def parse_url_params(self) -> dict:
        result = {}
        for param in self.supported_params:
            try:
                value = request.args.get(param[0])
                result[param[0]] = param[1](value) if value else None
            except ValueError:
                raise BadRequest(Translator.localize("cannot_parse_url_params"))

        return result

    def get_schema_name(self, schema_name: str) -> str:
        output = request.args.get("output")
        if not output or output.lower() == "default" or output.lower() not in self.output_types:
            return schema_name
        return f"{schema_name}{output.capitalize()}"

    def result(self, data: list, message=None) -> dict:
        if data and "items" in data[0]:
            data = data.pop(0)
            result = {}
            for key, value in data.items():
                result[key] = value
        else:
            result = {"items": data}
        result["message"] = message
        return result

    @staticmethod
    def set_request_language(language):
        if not language:
            language = "cs"
        elif isinstance(language, str):
            language = language
        else:
            language = language.code
        request.__setattr__("language", language)

    @staticmethod
    def rollback(entities: [BaseModel]):
        for entity in entities:
            if entity:
                entity.delete()

    def emit_websocket_notification(self, event_url: str, data: dict):
        url = f"{current_app.config['WEBSOCKET_URL']}/{event_url}"
        try:
            requests.post(url, json=data)
        except Exception:
            logger.error(f"websocket notification failed on {url}")

    @property
    def current_user(self) -> Optional[User]:
        return getattr(request, "current_user", None)
