from flask import request, jsonify
from flask_restx import Resource

from ..utilities.dto import bookDto
from ..service.bookService import get_all_books, get_book, get_book_by_title, new_book, delete_book, delete_book_title, update_book
from typing import Dict, Tuple

api_book = bookDto.api
_book = bookDto.book


@api_book.route('/book')
class BookList(Resource):
    @api_book.doc('List of Books')
    @api_book.marshal_list_with(_book, envelope='data')
    def get(self):
        """List all books"""
        return get_all_books()

    @api_book.expect(_book, validate=True)
    @api_book.response(201, 'Book successfully added.')
    @api_book.doc('Add a new book')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new book """
        data = request.json
        return new_book(data=data)


@api_book.route('/book/<isbnCode>')
@api_book.param('isbnCode', 'The ISBN Code for book')
@api_book.response(404, 'Book not found.')
class Book(Resource):
    @api_book.doc('get a book')
    @api_book.marshal_with(_book)
    def get(self, isbnCode):
        """get a book given its isbn"""
        book = get_book(isbnCode)
        if not book:
            api_book.abort(404)
        else:
            return book

    @api_book.doc('delete a book using isbn')
    @api_book.marshal_with(_book)
    def delete(self, isbnCode):
        """delete a book given its isbn"""
        book = get_book(isbnCode)
        if not book:
            api_book.abort(404)
        else:
            return delete_book(isbnCode)

    @api_book.doc('update a book using isbn')
    @api_book.expect(_book, validate=True)
    @api_book.marshal_with(_book)
    def patch(self, isbnCode):
        """update a book by navigating using isbnCode"""
        data = request.json
        book = get_book(isbnCode)
        if not book or data:
            api_book.abort(404)
        else:
            return update_book(data)


@api_book.route('/book/<title>')
@api_book.param('title', 'The title for book')
@api_book.response(404, 'Book not found.')
class BookName(Resource):

    @api_book.doc('get a book using title')
    @api_book.marshal_with(_book)
    def get(self, title):
        """get a book given its isbn"""
        book = get_book(title)
        if not book:
            api_book.abort(404)
        else:
            return book

    @api_book.doc('delete a book using title')
    @api_book.marshal_with(_book)
    def delete(self, title):
        """delete a book using title"""
        book = get_book(title)
        if not book:
            api_book.abort(404)
        else:
            return delete_book_title(title)

    @api_book.doc('update a book using title')
    @api_book.expect(_book, validate=True)
    @api_book.marshal_with(_book)
    def update(self, title):
        """update a book"""
        data = request.json
        book = get_book_by_title(title)
        if not book or data:
            api_book.abort(404)
        else:
            return update_book(data)
