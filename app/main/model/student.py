import datetime
import jwt
from typing import List, Union

from .. import db, flask_bcrypt
from ..config import key


class Student(db.Model):
    """ Student Model for storing Student related details """
    privateId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studentId = db.Column(db.Integer, unique=True)
    studentName = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    dateofBirth = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255))

    @classmethod
    def find_by_name(cls, name) -> "Student":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Student":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Student"]:
        return cls.query.all()

    @staticmethod
    def token_encode(studentId: int) -> bytes:
        try:
            to_be_encoded = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': studentId
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
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Student '{}'>".format(self.studentName)
