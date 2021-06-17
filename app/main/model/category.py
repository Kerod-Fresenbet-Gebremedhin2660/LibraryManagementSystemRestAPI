from typing import List

from .. import db


class Category(db.Model):
    """ Category Model for representing and storing Categories for Books """
    categoryId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoryName = db.Column(db.String(255), nullable=False, unique=True)
    books = db.relationship('Book', backref='', uselist=False)

    @classmethod
    def find_by_name(cls, name) -> "Category":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Category":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Category"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
