import pkgutil
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from logger import logger


for importer, modname, ispkg in pkgutil.walk_packages(__path__, __name__ + "."):
    # import all schema classes into globals
    exec(f"from {modname} import *")


def serialize(schema: str, data, many=True, **kwargs):
    """
    Returns serialized data collection of the schema. All schemas have to be imported in this file.

    :param schema: string name of marshmallow scheme of desired model
    :type schema: str
    :param data: model collection to be serialized
    :type many: bool
    :param many: decides output of serialization function - array or object
    :param kwargs: parameters passed to constructor of the scheme
    :return: serialized collection
    """
    klass = globals()[schema]
    data = data if isinstance(data, list) else [data]
    json_data = klass(many=True, **kwargs).dump(data)
    return json_data[0] or {} if not many and len(json_data) else json_data


def deserialize(schema: str, data: dict, **kwargs) -> dict:
    try:
        klass = globals()[schema]
        return klass(**kwargs).load(data)
    except ValidationError as e:
        logger.bind(exc_info=e)
        raise BadRequest(e.normalized_messages())
