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


class BaseIdModel(BaseModel):
    """
    A base model class that includes an integer primary key column named 'id' and a class method to retrieve an instance by its id.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, implicit_returning=False)

    @classmethod
    def get_by_id(cls: Type[T], id_: int) -> T:
        """
        Retrieve an instance of the model by its id.

        Args:
            id_: The id of the instance to retrieve.

        Returns:
            An instance of the model with the specified id, or None if no such instance exists.
        """
        return cls.query.filter_by(id=id_).first()


class BaseTimeModel(BaseModel):
    """
    A base model class that includes created_on and updated_on columns with default values.
    """

    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
