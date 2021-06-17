from typing import List

from .. import db


class Book(db.Model):
    """ Book Model for representing and storing books """
    isbnCode = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)
    totalCopies = db.Column(db.Integer, nullable=False)
    availableCopies = db.Column(db.Integer, nullable=False)
    publicationYear = db.Column(db.String(255), nullable=False)
    categoryId = db.Column(db.Integer, db.ForeignKey('category.categoryId'))
    authorId = db.Column(db.Integer, db.ForeignKey('author.authorId'))

    @classmethod
    def find_by_name(cls, name) -> "Book":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Book":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Book"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Book '{}'>".format(self.title)
