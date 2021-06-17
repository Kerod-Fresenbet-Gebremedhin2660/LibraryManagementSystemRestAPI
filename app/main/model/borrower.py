from typing import List

from .. import db


class Borrower(db.Model):
    """ Borrower Model for storing Students who are borrowers """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    borrowerId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    bookId = db.Column(db.Integer, db.ForeignKey('book.isbnCode'))
    dateofBorrow = db.Column(db.DateTime, nullable=False)
    BorrowedTo = db.Column(db.DateTime, nullable=False)
    actualReturnDate = db.Column(db.DateTime, nullable=False)

    # Foreign Keys
    issuedBy = db.Column(db.Integer, db.ForeignKey('staff.staffId'))
    book = db.relationship('Book', backref='borrower', lazy=True)

    @classmethod
    def find_by_name(cls, name) -> "Borrower":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "Borrower":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Borrower"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
