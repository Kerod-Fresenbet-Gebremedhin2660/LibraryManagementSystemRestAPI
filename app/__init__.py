from flask_restx import Api
from flask import Blueprint

from .main.controller.studentController import api_student as student_ns
from .main.controller.bookController import api_book as book_ns
from .main.controller.staffController import api_staff as staff_ns
from .main.controller.authorController import api_author as author_ns
from .main.controller.borrowerController import api_borrower as borrower_ns
from .main.controller.categoryController import api_category as category_ns
from .main.controller.authControllerStudent import api as auth_ns
from .main.controller.authControllerStaff import api as auth_staff_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='API for Library Management System',
    version='1.0',
    description='Flask RestX LMS API',
    security='apikey'
)

api.add_namespace(student_ns, path='/api/v1')
api.add_namespace(book_ns, path='/api/v1')
api.add_namespace(staff_ns, path='/api/v1')
api.add_namespace(author_ns, path='/api/v1')
api.add_namespace(borrower_ns, path='/api/v1')
api.add_namespace(category_ns, path='/api/v1')
api.add_namespace(auth_ns, path='/api/v1')
api.add_namespace(auth_staff_ns, path='/api/v1')

