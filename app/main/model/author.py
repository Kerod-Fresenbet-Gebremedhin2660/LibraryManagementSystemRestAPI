from typing import List

from .. import db


class Author(db.Model):
    """ Author Model for representing and storing Authors """
    authorId = db.Column(db.Integer, primary_key=True)
    authorName = db.Column(db.String, nullable=False)

    book = db.relationship('Book', backref='author', uselist=False, lazy=True)

    @classmethod
    def find_by_name(cls, name) -> "Author":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Author":
        return cls.query.filter_by(id=_id).first()

    # Shortcuts
    @classmethod
    def find_all(cls) -> List["Author"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
