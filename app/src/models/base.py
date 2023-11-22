from typing import Type, TypeVar
import sqlalchemy
from werkzeug.exceptions import BadRequest, InternalServerError
from src.translations.translator import Translator

from logger import logger
from src.models import db

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model):
    """
    Base model for all database models.
    """

    __abstract__ = True

    def save(self):
        """
        Saves the current instance to the database.

        Raises:
            BadRequest: If a unique constraint is violated.
            InternalServerError: If any other error occurs during the save operation.
        """
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
        """
        Deletes the current instance from the database.

        Raises:
            InternalServerError: If there was an error deleting the instance from the database.
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            logger.bind(exc_info=e)
            raise InternalServerError(str(e))

    @classmethod
    def get_items(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls: Type[T], id_: int) -> T:
        return cls.query.filter_by(id=id_).first()

    @classmethod
    def get_by_code(cls: Type[T], code_: str) -> T:
        return cls.query.filter_by(code=code_).first()


class BaseIdModel(BaseModel):
    """
    A base model class that includes an integer primary key column named 'id' and a class method to retrieve an instance by its id.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, implicit_returning=False)
    active = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return str(self.__dict__)


class Transaction:
    """
    A class representing a transaction for database operations.

    Attributes:
        session (Session): The database session.
        items_count (int): The count of items in the transaction.
        bulk_size (int): The size at which the transaction should be flushed.

    Methods:
        flush_bulk(): Flushes the transaction if the item count exceeds the bulk size.
        add(*entities): Adds entities to the transaction.
        merge(*entities): Merges entities into the transaction.
        remove(*entities): Removes entities from the transaction.
        commit(): Commits the transaction to the database.
    """

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
