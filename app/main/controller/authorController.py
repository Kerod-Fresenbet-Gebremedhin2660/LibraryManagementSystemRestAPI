from flask import request, jsonify
from flask_restx import Resource

from ..utilities.dto import authorDto
from ..service.authorService import new_author, get_all_authors, get_author, delete_author, update_author

api_author = authorDto.api
_author = authorDto.author


@api_author.route('/author')
class AuthorList(Resource):
    @api_author.doc('List of Authors')
    @api_author.marshal_list_with(_author, envelope='data')
    def get(self):
        """List all authors"""
        authors = get_all_authors()
        return authors

    @api_author.expect(_author, validate=True)
    @api_author.response(201, 'Author successfully added.')
    @api_author.doc('Add a new Author')
    def post(self):
        """Creates a new Author"""
        data = request.json
        return new_author(data=data)


@api_author.route('/author/<author_id>')
@api_author.param('authorId', 'The AuthorId of an Author')
@api_author.response(404, 'Author Not Found.')
class AuthorID(Resource):
    @api_author.doc('get an author')
    @api_author.marshal_with(_author)
    def get(self, authorId):
        """get an author given their authorId"""
        author = get_author(authorId)
        if not author:
            api_author.abort(404)
        else:
            return author

    @api_author.doc('delete an author')
    @api_author.marshal_with(_author)
    def delete(self, authorId):
        """delete an author using authorId"""
        return delete_author(authorId)

    @api_author.doc('update an author')
    @api_author.expect(_author, validate=True)
    def update(self, authorId):
        """update an author by navigating using the author id"""
        data = request.json
        return update_author(data)


@api_author.route('/author/<author_name>')
@api_author.param('authorName', 'The AuthorName of an Author')
@api_author.response(404, 'Author Not Found.')
class AuthorName(Resource):
    @api_author.doc('get an author')
    @api_author.marshal_with(_author)
    def get(self, authorName):
        """get an author given their authorId"""
        author = get_author(authorName)
        if not author:
            api_author.abort(404)
        else:
            return author

    @api_author.doc('update an author using the author name')
    @api_author.expect(_author, validate=True)
    @api_author.marshal_with(_author)
    def update(self, authorName):
        """update an author by navigating using the author name"""
        data = request.json
        return update_author(data)

