import jwt
import datetime
from typing import List, Union
from ..config import key
from .. import db, flask_bcrypt


class Staff(db.Model):
    privateId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staffId = db.Column(db.Integer, unique=True)
    email = db.Column(db.String, unique=True)
    staffName = db.Column(db.String(255), nullable=False, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    hashPassword = db.Column(db.String(255), nullable=False, unique=True)

    @classmethod
    def find_by_name(cls, staffName) -> "Staff":
        return cls.query.filter_by(staffName=staffName).first()

    @classmethod
    def find_by_id(cls, _id) -> "Staff":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Staff"]:
        return cls.query.all()

    @staticmethod
    def token_encode(staffId: int) -> bytes:
        try:
            to_be_encoded = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': staffId
            }
            return jwt.encode(
                to_be_encoded, key, algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def token_decode(token: str) -> Union[str, int]:
        try:
            decoded = jwt.decode(token, key)
            return decoded['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.hashPassword = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Staff '{}'>".format(self.staffName)
