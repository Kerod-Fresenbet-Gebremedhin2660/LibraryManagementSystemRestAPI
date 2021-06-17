from flask import request, jsonify
from flask_restx import Resource

from ..utilities.dto import categoryDto
from ..service.categoryService import new_category, get_all_categories, get_category, delete_category, update_category
from typing import Dict, Tuple
from ..utilities.decorator import staff_token_required, token_required

api_category = categoryDto.api
_category = categoryDto.category


@api_category.route('/category')
class categoryList(Resource):
    @api_category.doc('List of categories')
    @api_category.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all categories"""
        return get_all_categories()

    @api_category.expect(_category, validate=True)
    @api_category.response(201, 'category successfully added.')
    @api_category.doc('Add a new category')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new category"""
        data = request.json
        return new_category(data=data)


@api_category.route('/category/<categoryId>')
@api_category.param('categoryId', 'The categoryId of a category')
@api_category.response(404, 'category Not Found.')
class category(Resource):
    @api_category.doc('get a category')
    @api_category.response(200, 'category successfully retrieved.')
    @api_category.marshal_with(_category)
    def get(self, categoryId):
        """get a category given its categoryId"""
        cat = get_category(categoryId)
        if not category:
            api_category.abort(404)
        else:
            return cat

    @api_category.doc('update a category')
    @api_category.expect(_category, validate=True)
    @api_category.marshal_with(_category)
    def patch(self, categoryId):
        """update a category navigating using its categoryId"""
        data = request.json
        if not data:
            api_category.abort(404)
        else:
            return update_category(data)

    @api_category.doc('delete a category')
    @api_category.param('categoryId', 'The categoryId')
    @api_category.marshal_with(_category)
    def delete(self, categoryId):
        """delete a category given its categoryId"""
        return delete_category(categoryId)


