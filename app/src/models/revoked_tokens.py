from src.models import db
from src.models.base import BaseIdModel


class RevokedToken(BaseIdModel):
    __tablename__ = "revoked_tokens"

    jti = db.Column(db.String(120))

    @classmethod
    def is_jti_blocklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
