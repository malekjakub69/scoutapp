from flask_jwt_extended import jwt_required
from src.models.base import Transaction
from src.resources.base import BaseResource

from src.models.check_member import CheckMember
from src.schemas import deserialize, serialize
from src.translations.translator import Translator
from flask_restful import request
from werkzeug.exceptions import NotFound
from src.authorization.decorators import authorize_all


class CheckMembersResource(BaseResource):
    @authorize_all()
    def get(self):
        check_members = CheckMember.get_items()
        return self.result(serialize("CheckMemberSchema", check_members))


class CheckMemberByHashResource(BaseResource):
    @jwt_required()
    def get(self, member_hash: str):
        check_members = CheckMember.get_by_member_hash(member_hash)
        return self.result(serialize("CheckMemberSchema", check_members))


class CheckMemberResource(BaseResource):
    @jwt_required()
    def get(self, check_member_id: int):
        check_member = CheckMember.get_by_id(check_member_id)
        return self.result(serialize("CheckMemberSchema", check_member))

    @jwt_required()
    def post(self):
        data = deserialize("CheckMemberSchema", request.get_json())
        transaction = Transaction()
        check_member = CheckMember(**data)
        transaction.add(check_member)
        transaction.commit()
        return (self.result(serialize("CheckMemberSchema", check_member)), 201)

    @jwt_required()
    def delete(self, check_member_id: int):
        if not (check_member := CheckMember.get_by_id(check_member_id)):
            raise NotFound(Translator.localize("entity_not_found"))
        check_member.delete()
        return {"check_member:": Translator.localize("entity_deleted", check_member_id)}
