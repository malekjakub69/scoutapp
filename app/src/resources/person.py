from flask_jwt_extended import jwt_required
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.person import Person
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class PersonsResource(BaseResource):
    @authorize_all()
    def get(self):
        persons = Person.get_items()
        return self.result(serialize("PersonSchema", persons))


class PersonResource(BaseResource):
    @jwt_required()
    def get(self, person_id: int):
        person = Person.get_by_id(person_id)
        return self.result(serialize("PersonSchema", person))

    @jwt_required()
    def post(self):
        data = deserialize("PersonSchema", request.get_json())
        transaction = Transaction()
        person = Person(**data)
        transaction.add(person)
        transaction.commit()

        return (self.result(serialize("PersonSchema", person)), 201)

    @jwt_required()
    def delete(self, person_id: int):
        if not (person := Person.get_by_id(person_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        person.delete()
        return {"person:": Translator.localize("entity_deleted", person_id)}
