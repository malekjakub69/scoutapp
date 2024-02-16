from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.role import Role
from src.models.unit import Unit
from src.models.user import User
from app.src.models.person import Person
from src.models.points import Points
from src.models.meet import Meet
from src.models.register import Register
from src.models.check_person import CheckPerson
from src.models.permission import Permission
from src.models.revoked_tokens import RevokedToken

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:MyV3ryS3cr3t3Passw0rd@db:5432/ScoutApp"
db = SQLAlchemy(app)


def reset_database():
    # Vymažeme všechny tabulky
    try:
        db.session.query(RevokedToken).delete()
        db.session.query(CheckPerson).delete()
        db.session.query(Register).delete()
        db.session.query(Meet).delete()
        db.session.query(Points).delete()
        db.session.query(Person).delete()
        db.session.query(Permission).delete()
        db.session.query(Role).delete()
        db.session.query(User).delete()
        db.session.query(Unit).delete()

        db.session.commit()
    except:
        db.session.rollback()
        raise "Error"


if __name__ == "__main__":
    with app.app_context():
        reset_database()
