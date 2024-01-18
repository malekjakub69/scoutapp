from flask_jwt_extended import jwt_required
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.member import Member
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class MembersResource(BaseResource):
    @authorize_all()
    def get(self):
        members = Member.get_items()
        return self.result(serialize("MemberSchema", members))


class MemberResource(BaseResource):
    @jwt_required()
    def get(self, member_id: int):
        member = Member.get_by_id(member_id)
        return self.result(serialize("MemberSchema", member))

    @jwt_required()
    def post(self):
        data = deserialize("MemberSchema", request.get_json())
        transaction = Transaction()
        member = Member(**data)
        transaction.add(member)
        transaction.commit()

        return (self.result(serialize("MemberSchema", member)), 201)

    @jwt_required()
    def delete(self, member_id: int):
        if not (member := Member.get_by_id(member_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        member.delete()
        return {"member:": Translator.localize("entity_deleted", member_id)}
