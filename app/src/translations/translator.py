import json

from flask_restful import request

from src.utils.utils import get_absolute_path


class Translator:
    with open(get_absolute_path(__file__, "../en.json"), "r") as en_file:
        en = json.load(en_file)
    with open(get_absolute_path(__file__, "../cs.json"), "r") as cs_file:
        cs = json.load(cs_file)

    @classmethod
    def localize(cls, key: str, *args, capitalize=True) -> str:
        language = request.language if hasattr(request, "language") else "cs"
        if language not in cls.__dict__:
            language = "cs"
        try:
            text = eval(f"cls.{language}")[key.lower()].format(*args)
            return text.capitalize() if capitalize else text
        except KeyError:
            return key
        except AttributeError:
            return "Translator error."
