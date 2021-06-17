from app.main import db
from app.main.model.author import Author


def new_author(data):
    author = Author.query.filter_by(authorId=data['authorId']).first()
    if not author:
        newAuthor = Author(
            authorId=data['authorId'],
            authorName=data['authorName']
        )
        save_changes(newAuthor)
        response_object = {
            'status': 'success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Author already in the system',
        }
        return response_object, 409


def update_author(data):
    author = Author.query.filter_by(authorId=data['authorId']).first()
    if author:
        updatedAuthor = author(
            authorId=data['authorId'],
            authorName=data['authorName']
        )
        save_changes(updatedAuthor)
        response_object = {
            'status': 'success',
            'message': 'Successfully Updated.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Updated Failed',
        }
        return response_object, 409


def delete_author(authorId):
    author = get_author(authorId)
    return author.delete_from_db()


def get_all_authors():
    return Author.query.all()


def get_author(authorId):
    return Author.query.filter_by(authorId=authorId).first()


def get_author_name(authorName):
    return Author.query.filter_by(authorName=authorName).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
