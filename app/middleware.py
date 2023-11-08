from flask_restful import request

from logger import logger


def before_request():
    # delete old logger
    logger.new()


def after_request(response):
    context = {
        "endpoint": request.url,
        "method": request.method,
        "status_code": response.status_code,
        "url_args": request.args.to_dict(),
        "view_args": request.view_args,
        "payload": request.get_json(silent=True),
        "ip": request.headers.get("X-Real-IP", request.remote_addr),
        "response": response.get_json(silent=True),
    }
    if context["status_code"] < 400:
        logger.info("response", **context)
    elif context["status_code"] < 500:
        logger.warning("response", **context)
    else:
        logger.error("response", **context)

    return response
