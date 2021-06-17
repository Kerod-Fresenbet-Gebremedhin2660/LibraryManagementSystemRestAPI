from flask_restx import Namespace, fields


class studentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        'studentName': fields.String(required=True, description='student name'),
        'email': fields.String(required=True, description='student email address'),
        'sex': fields.String(required=True, description='student sex'),
        'dateofBirth': fields.String(required=True, description='student date of birth'),
        'department': fields.String(required=True, description='student department'),
        'password_hash': fields.String(required=True, description='student password')
    })


class bookDto:
    api = Namespace('book', description='book related operations')
    book = api.model('book', {
        'isbnCode': fields.Integer(required=True, description='isbn code for book'),
        'title': fields.String(required=True, description='title for book'),
        'language': fields.String(required=True, description='language for book'),
        'totalCopies': fields.Integer(required=True, description='total copies available for the book'),
        'availableCopies': fields.Integer(required=True, description='book copies available'),
        'publicationYear': fields.String(required=True, description='publication year of book'),
        'categoryId': fields.Integer(required=True, description='the category identifier of the book'),
        'authorId': fields.Integer(required=True, descripton='the book author id')
    })


class authorDto:
    api = Namespace('author', description='author related operations')
    author = api.model('author', {
        'authorId': fields.Integer(required=True, description='The Authors ID'),
        'authorName': fields.String(required=True, description='The Authors Name')
    })


class categoryDto:
    api = Namespace('category', description='category related operations')
    category = api.model('category', {
        'categoryName': fields.String(required=True, description='The cataegory Name')
    })


class borrowDto:
    api = Namespace('borrower', description='borrower related operation')
    borrower = api.model('borrower', {
        'borrowerId': fields.String(required=True, description='the borrower Id'),
        'bookId': fields.String(required=True, description='the borrowed book Id'),
        'dateofBorrow': fields.String(required=True, description='the date of the borrowed'),
        'BorrowedTo': fields.String(required=True, description='the date to it is going to be returned'),
        'actualReturnDate': fields.String(required=True, descritption='the date it actually got returned'),
        'issuedBy': fields.String(required=True, description='the issuer of the borrow operation'),
    })


class staffDto:
    api = Namespace('staff', description='staff related operation')
    staff = api.model('staff', {
        'staffName': fields.String(required=True, description='name of the staff'),
        'email': fields.String(required=True, description='email of the staff'),
        'registered_on': fields.String(required=True, description='date of registration'),
        'hashPassword': fields.String(required=True, description='password hash')
    })


# Authentication
class authDto:
    # Two classes of Users need to be authenticated
    # Two classes of tokens is required as well
    # One will be authorized to perform certain special functions
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='the email address'),
        'password': fields.String(required=True, description='the user password '),
    })
