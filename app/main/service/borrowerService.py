import datetime

from app.main import db
from app.main.model.borrower import Borrower


def new_borrower(data):
    borrower = Borrower.query.filter_by(email=data['email']).first()
    if not borrower:
        newBorrower = Borrower(
            borrowerId=data['borrowerId'],
            bookId=data['bookId'],
            dateofBorrow=datetime.datetime.utcnow(),
            borrowedTo=data['borrowedTo'],
            actualReturnDate=data['actualReturnDate'],
            issuedBy=data['issuedBy']
        )
        save_changes(newBorrower)
        response_object = {
            'status': 'success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Borrow quota reached.',
        }
        return response_object, 409


def update_borrower(data):
    borrower = Borrower.query.filter_by(email=data['email']).first()
    if borrower:
        borrower.borrowerId = data['borrowerId']
        borrower.bookId = data['bookId']
        borrower.dateofBorrow = datetime.datetime.utcnow()
        borrower.borrowedTo = data['borrowedTo']
        borrower.actualReturnDate = data['actualReturnDate']
        borrower.issuedBy = data['issuedBy']
        save_changes(borrower)
        response_object = {
            'status': 'success',
            'message': 'Successfully Updated.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Borrow update failed.',
        }
        return response_object, 404


def get_all_borrowers():
    return Borrower.query.all()


def get_user(borrowerId):
    return Borrower.query.filter_by(borrowerId=borrowerId).first()


def get_user_by_email(email):
    return Borrower.query.filter_by(email=email).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
