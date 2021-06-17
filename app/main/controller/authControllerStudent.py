from flask import request
from flask_restx import Resource

from app.main.service.authHelper import Auth
from ..utilities.dto import authDto
from typing import Dict, Tuple

api = authDto.api
user_auth = authDto.user_auth


@api.route('/login')
class StudentLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        # get the post data
        auth_details = request.json
        return Auth.login_user(data=auth_details)


@api.route('/logout')
class StudentLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self) -> Tuple[Dict[str, str], int]:
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
