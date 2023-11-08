import logging
import os

import structlog
from flask_restful import request
from structlog import DropEvent

_structlog_proxy = structlog.get_logger()


def add_user_info(_, __, event_dict: dict) -> dict:
    if "user_id" not in event_dict.keys():
        event_dict["user_id"] = request.user if hasattr(request, "user") else None
    return event_dict


def format_response(_, __, event_dict: dict) -> dict:
    response = event_dict.pop("response", {})
    if response and isinstance(response, dict) and "message" in response.keys():
        event_dict["response_message"] = response.pop("message")
    # event_dict["response"] = response  # log full response
    return event_dict


def remove_exceptions(_, method: str, event_dict: dict) -> dict:
    if method == "info" and "exception" in event_dict.keys():
        event_dict.pop("exception", None)
    return event_dict


def drop_options_method(_, __, event_dict: dict):
    if event_dict.get("method") == "OPTIONS":
        raise DropEvent
    return event_dict


class StructlogLogger:
    @classmethod
    def configure(cls, component: str, *args, **kwargs) -> "StructlogLogger":
        structlog.configure_once(
            cache_logger_on_first_use=True,
            context_class=structlog.threadlocal.wrap_dict(dict),
            logger_factory=structlog.PrintLoggerFactory(),
            wrapper_class=structlog.make_filtering_bound_logger(cls.__get_loging_level()),
            processors=[
                # The order of processors is very important
                drop_options_method,
                format_response,
                add_user_info,
                structlog.stdlib.add_log_level,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", key="time", utc=False),
                structlog.processors.format_exc_info,
                structlog.processors.ExceptionPrettyPrinter(),  # for dev purposes only!
                remove_exceptions,
                structlog.processors.JSONRenderer(),
            ],
        )

        return cls()

    # Log levels

    def critical(self, event: str, **kwargs) -> None:
        _structlog_proxy.critical(event, **kwargs)

    def debug(self, event: str, **kwargs) -> None:
        _structlog_proxy.debug(event, **kwargs)

    def error(self, event: str, **kwargs) -> None:
        _structlog_proxy.error(event, **kwargs)

    def exception(self, event: str, **kwargs) -> None:
        _structlog_proxy.exception(event, **kwargs)

    def info(self, event: str, **kwargs) -> None:
        _structlog_proxy.info(event, **kwargs)

    def warning(self, event: str, **kwargs) -> None:
        _structlog_proxy.warning(event, **kwargs)

    def bind(self, **kwargs) -> "StructlogLogger":
        return _structlog_proxy.bind(**kwargs)

    def new(self, **kwargs) -> "StructlogLogger":
        return _structlog_proxy.new(**kwargs)

    @staticmethod
    def __get_loging_level():
        levels_map = {
            "debug": logging.DEBUG,
            "info": logging.INFO,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.CRITICAL,
        }
        level = os.environ.get("LOGGING_LEVEL", "info")
        if level in levels_map.keys():
            return levels_map[level]
        return logging.INFO


logger = StructlogLogger()
