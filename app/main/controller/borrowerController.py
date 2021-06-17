from flask import request, jsonify
from flask_restx import Resource
from ..utilities.dto import borrowDto
from ..service.borrowerService import get_all_borrowers, get_user, new_borrower
from typing import Dict, Tuple

api_borrower = borrowDto.api
_borrower = borrowDto.borrower


@api_borrower.route('/borrower')
class BorrowerList(Resource):
    @api_borrower.doc('List of Borrowers')
    @api_borrower.response(200, 'Borrowers successfully retrieved.')
    @api_borrower.marshal_list_with(_borrower, envelope='data')
    def get(self):
        return get_all_borrowers()

    @api_borrower.expect(_borrower, validate=True)
    @api_borrower.response(201, 'Borrower successfully recorded.')
    @api_borrower.doc('Add a new borrower')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new borrower """
        data = request.json
        return new_borrower(data=data)


@api_borrower.route('/borrower/<borrowerId>')
@api_borrower.param('borrowerId', 'id of the user that borrowed a book')
@api_borrower.response(404, 'borrower not found')
class Borrower(Resource):
    @api_borrower.doc('get a borrower')
    @api_borrower.response(200, 'Borrower successfully retrieved.')
    @api_borrower.marshal_with(_borrower)
    def get(self, borrowerId):
        borrower = get_user(borrowerId)
        if not borrower:
            api_borrower.abort(404)
        else:
            return borrower

    @api_borrower.expect()
    @api_borrower.response(404, 'Resource Not Found')
    @api_borrower.marshal_with(_borrower)
    def update(self, borrowerId):
        @api_borrower.expect(_borrower, validate=True)
        @api_borrower.response(201, 'Book successfully borrowed.')
        @api_borrower.doc('borrow a book')
        def post():
            data = request.json
            return new_borrower(data=data)
