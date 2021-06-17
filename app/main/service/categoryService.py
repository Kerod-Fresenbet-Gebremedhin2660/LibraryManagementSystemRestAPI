import uuid
from app.main import db
from app.main.model.category import Category


def new_category(data):
    category = Category.query.filter_by(categoryId=data['categoryId']).first()
    if not category:
        newCategory = Category(
            categoryId=uuid.uuid4(),
            categoryName=data['categoryName']
        )
        save_changes(newCategory)
        response_object = {
            'status': 'Success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Category Already In the System',
        }
        return response_object, 409


def update_category(data):
    category = Category.query.filter_by(categoryId=data['categoryId']).first()
    if category:
        category.categoryId = data['categoryId']
        category.categoryName = data['categoryName']
        save_changes(category)
        response_object = {
            'status': 'success',
            'message': 'Successfully Updated.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Category Doesn\'t exist in the system',
        }
        return response_object, 404


def delete_category(categoryId):
    if get_category(categoryId):
        Category.delete_from_db()
    else:
        response_object = {
            'status': 'fail',
            'message': 'Category Doesn\'t exist in the system'
        }
        return response_object, 404


def get_all_categories():
    if Category.query.all():
        return Category.query.all()
    else:
        response_object = {
            'status': 'fail',
            'message': 'No Categories Exist in the system.'
        }
        return response_object


def get_category(categoryId):
    if Category.query.filter_by(categoryId=categoryId).first():
        return Category.query.filter_by(categoryId=categoryId).first()
    else:
        response_object = {
            'status': 'fail',
            'message': 'No Such Category exists in the system.'
        }
        return response_object


def get_category_name(categoryName):
    if Category.query.filter_by(categoryName=categoryName).first():
        return Category.query.filter_by(categoryName=categoryName).first()
    else:
        response_object = {
            'status': 'fail',
            'message': 'No Categories Exist in the system.'
        }
        return response_object


def save_changes(data):
    db.session.add(data)
    db.session.commit()
