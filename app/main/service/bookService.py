from app.main import db
from app.main.model.book import Book


def new_book(data):
    book = Book.query.filter_by(isbnCode=data['isbnCode']).first()
    if not book:
        newBook = Book(
            isbnCode=data['isbnCode'],
            title=data['title'],
            language=data['language'],
            totalCopies=data['totalCopies'],
            availableCopies=data['availableCopies'],
            publicationYear=data['publicationYear'],
            categoryId=data['categoryId'],
            authorId=data['authorId'],
        )
        save_changes(newBook)
        response_object = {
            'status': 'Success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Book already in the system.',
        }
        return response_object, 409


def update_book(data):
    book = Book.query.filter_by(isbn=data['isbn']).first()
    if book:
        book.isbnCode = data['isbnCode']
        book.title = data['title']
        book.language = data['language']
        book.totalCopies = data['totalCopies']
        book.availableCopies = data['availableCopies']
        book.publicationYear = data['publicationYear']
        book.categoryId = data['categoryId']
        book.authorId = data['authorId']
        save_changes(book)
        response_object = {
            'status': 'success',
            'message': 'Successfully Updated.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Update Failed',
        }
        return response_object, 409


def get_all_books():
    return Book.query.all()


def get_book(isbnCode):
    return Book.query.filter_by(isbnCode=isbnCode).first()


def get_book_by_title(title):
    return Book.query.filter_by(title=title).first()


def delete_book(isbnCode):
    book = get_book(isbnCode)
    if book:
        return book.delete_from_db()
    else:
        return {"message": "Book doesn't exist"}, 404


def delete_book_title(title):
    book = get_book_by_title(title)
    return book.delete_from_db()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
