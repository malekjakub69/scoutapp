from flask_jwt_extended import get_jwt_identity, jwt_required
from src.models.unit import Unit
from src.models.register import Register
from src.models.user import User
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
        # 1 přihlášený uživatel
        logged_user: User = User.get_by_email_or_login(get_jwt_identity())

        avaliable_all_unit_ids = Unit.get_avaliable_unit_ids(logged_user)

        registers = Register.get_by_units(avaliable_all_unit_ids)
        persons = [register.person for register in registers]
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
