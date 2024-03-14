from flask_jwt_extended import get_jwt_identity, jwt_required
from src.models.unit import Unit
from src.models.user import User
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.check_person import CheckPerson
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class CheckPersonsResource(BaseResource):
    @authorize_all()
    def get(self, meet_id: int):
        check_persons = CheckPerson.get_by_meet_id(meet_id)
        return self.result(serialize("CheckPersonSchema", check_persons))


class CheckPersonByHashResource(BaseResource):
    @jwt_required()
    def get(self, person_hash: str):
        check_persons = CheckPerson.get_by_person_hash(person_hash)
        return self.result(serialize("CheckPersonSchema", check_persons))

    def put(self, id: int):
        data = deserialize("CheckPersonConfirmSchema", request.get_json())
        check: CheckPerson = CheckPerson.get_by_id(id)
        check.sent = True
        check.confirm = data["confirm"]
        check.no_reason = data["no_reason"]
        check.other_desc = data["other_desc"]
        check.save()
        return self.result(serialize("CheckPersonSchema", check))


class CheckPersonResource(BaseResource):
    @jwt_required()
    def get(self, check_person_id: int):
        check_person = CheckPerson.get_by_id(check_person_id)
        return self.result(serialize("CheckPersonSchema", check_person))

    @jwt_required()
    def post(self):
        data = deserialize("CheckPersonSchema", request.get_json())
        transaction = Transaction()
        check_person = CheckPerson(**data)
        transaction.add(check_person)
        transaction.commit()
        return (self.result(serialize("CheckPersonSchema", check_person)), 201)

    @jwt_required()
    def delete(self, check_person_id: int):
        if not (check_person := CheckPerson.get_by_id(check_person_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        check_person.delete()
        return {"check_person:": Translator.localize("entity_deleted", check_person_id)}
