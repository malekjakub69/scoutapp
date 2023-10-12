import datetime
import re
from typing import Type, TypeVar
from urllib.parse import unquote

import sqlalchemy.exc
from flask import current_app
from logger import logger
from pyodbc import DataError
from src.models import db
from src.translations.translator import Translator
from werkzeug.exceptions import BadRequest, InternalServerError

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        return self.to_dict()

    @classmethod
    def base_sort(cls) -> list:
        return []

    @classmethod
    def get_item_query(cls, user_filter: str, resource_filter):
        return cls.query.filter(db.text(user_filter))

    @classmethod
    def get_items(
        cls: Type[T], params: dict, default_params: dict, with_pagination=False, resource_filter=None
    ) -> dict:
        """
        Base method for getting items. It allows filtering, sorting and pagination. It can be parametrized by
        default class-specific filters.
        :param dict params: Dictionary of parsed URL parameters for filtering and sorting .
        :param dict default_params: Dictionary of default filtering values passed from calling method.
        :param bool with_pagination: Determines if result is paginated.
        :param tuple resource_filter: Resource-specific filter.
        :return: Paginated or all class items
        """
        _filter = ""
        for column, value in default_params.items():
            _filter += f"{column}={value} and "
        if "filter" in params and params["filter"] is not None:
            _filter += f"{cls.parse_filter(params['filter'])}"
        if _filter.endswith("and "):
            _filter = _filter[:-5]  # remove trailing "and "

        sort_query = cls.base_sort()
        if "sort" in params and params["sort"] is not None:
            sort_query = cls.parse_sort_query(params["sort"])

        try:
            # get filtrated and sorted items
            query = cls.get_item_query(_filter, resource_filter).order_by(*sort_query)
            if with_pagination:
                page = params["page"] if params["page"] is not None else 1
                pagination = query.paginate(
                    page=page,
                    per_page=params["limit"]
                    if params.get("limit") is not None
                    else current_app.config["DEFAULT_PAGINATION"],
                    max_per_page=current_app.config["MAX_PER_PAGE"],
                )
                return pagination
            else:
                return query.all()
        except DataError as e:
            # if isinstance(e.orig, driver_errors.InvalidTextRepresentation):
            #     logger.error("DB_data_error", exc_info=e)
            raise BadRequest(Translator.localize("invalid_filter_input_type"))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except sqlalchemy.exc.DBAPIError as e:
            if e.orig.args[0] == "23000":
                raise BadRequest(Translator.localize("db_key_exists"))
            db.session.rollback()
            logger.bind(exc_info=e)
            raise InternalServerError()
        except Exception as e:
            logger.bind(exc_info=e)
            db.session.rollback()
            raise InternalServerError("DB error")

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            logger.bind(exc_info=e)
            raise InternalServerError(str(e))

    @classmethod
    def parse_filter(cls, _filter: str) -> str:
        available_columns = [c_attrs.key for c_attrs in db.inspect(cls).mapper.column_attrs]
        available_operators = {
            "eq": "=",
            "like": " like ",
            "in": " in ",
            "lt": "<",
            "lte": "<=",
            "gt": ">",
            "gte": ">=",
            "neq": "<>",
        }
        query = ""
        pattern = r"^(\w+)~(\w+)~(.+)$"
        filters = _filter.split("|")
        delimiter = ","

        for f in filters:
            contains_null = False
            match = re.match(pattern, f)
            if not match:
                raise BadRequest(Translator.localize("invalid_filter_syntax"))
            key = match.group(1)
            if key not in available_columns:
                raise BadRequest(Translator.localize("key_not_for_filtration", key))
            try:
                operator = available_operators[match.group(2)]
                db_type = db.inspect(cls).mapper.columns[key].type.python_type
                value = str(unquote(match.group(3)))
                if match.group(2) == "like":
                    if db_type != str:
                        raise TypeError
                    value = f"'%{value}%'"
                elif match.group(2) == "in":
                    if "null" in value:
                        contains_null = True
                        value = delimiter.join([val for val in value.split(delimiter) if val != "null"])
                    if db_type != int or not cls._has_value_correct_type(value, int, is_list=True):
                        raise TypeError
                    value = value if value else "null"  # specialni pripad kdyz filtrujeme pouze null
                    value = f"({value})"
                else:
                    if not cls._has_value_correct_type(value, db_type):
                        raise TypeError
                    value = f"'{value}'"
            except KeyError:
                raise BadRequest(Translator.localize("invalid_filter_operator", match.group(2)))
            except ValueError:
                raise BadRequest(Translator.localize("invalid_filter_datatype"))
            except TypeError:
                raise BadRequest(Translator.localize("column_value_type_filter_error"))
            except Exception as e:
                logger.bind(exc_info=e)
                raise BadRequest(Translator.localize("generic_filter_query"))

            if contains_null:
                query += f"({key}{operator}{value} OR {key} IS NULL) and "
            else:
                query += f"{key}{operator}{value} and "

        query = query[:-5]  # remove trailing "and "
        return query

    @classmethod
    def parse_sort_query(cls, url_query: str) -> list:
        available_columns = [c_attrs.key for c_attrs in db.inspect(cls).mapper.column_attrs]
        query = []
        pattern = r"^(\w+)~(asc|desc)$"
        sort_params = url_query.split("|")

        for param in sort_params:
            match = re.match(pattern, param)
            if not match:
                raise BadRequest(Translator.localize("invalid_sort_syntax"))
            key = match.group(1)
            if key not in available_columns:
                raise BadRequest(Translator.localize("key_not_for_sort"))
            column = match.group(1)
            order = match.group(2)
            query.append(eval(f"cls.{column}.{order}()"))
        return query

    def to_dict(self):
        result = {}
        for column in self.__table__.columns:
            result[column.name] = str(getattr(self, column.name))
        return result

    @staticmethod
    def _has_value_correct_type(value, datatype: type, is_list=False, delimiter=","):
        columns2types = {datetime.datetime: str}
        column_type = datatype
        for possible_type in columns2types:
            if datatype == possible_type:
                column_type = columns2types[possible_type]

        if not is_list:
            return column_type(value)
        else:
            if not value:
                return True
            return all([column_type(value) for value in value.split(delimiter)])


class BaseIdModel(BaseModel):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def base_sort(cls) -> list:
        return [cls.id.desc()]

    @classmethod
    def get_by_id(cls: Type[T], id_: int) -> T:
        return cls.query.filter_by(id=id_).first()


class BaseTimeModel:
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def base_sort(cls) -> list:
        return [cls.created_on.desc()]


class Transaction:
    def __init__(self, bulk_size=100):
        self.session = db.session
        self.items_count = 0
        self.bulk_size = bulk_size

    def flush_bulk(self):
        if self.items_count >= self.bulk_size:
            self.commit()
            # logger.info(f"Flushing bulk of size {self.items_count}")
            self.items_count = 0

    def add(self, *entities):
        for entity in entities:
            self.session.add(entity)
            self.items_count += 1
        self.flush_bulk()

    def merge(self, *entities):
        for entity in entities:
            self.session.merge(entity)
            self.items_count += 1
        self.flush_bulk()

    def remove(self, *entities):
        for entity in entities:
            self.session.delete(entity)
            self.items_count += 1
        self.flush_bulk()

    def commit(self):
        try:
            self.session.commit()
            self.items_count = 0
        except sqlalchemy.exc.DBAPIError as e:
            if e.orig.args[0] == "23000":
                raise BadRequest(Translator.localize("db_key_exists"))
            logger.bind(exc_info=e)
            raise InternalServerError()
        except Exception as e:
            logger.bind(exc_info=e)
            raise InternalServerError("DB error")
        finally:
            self.session.rollback()
