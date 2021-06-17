from flask import request
from flask_restx import Resource

from app.main.service.authHelper import StaffAuth
from ..utilities.dto import authDto
from typing import Dict, Tuple

api = authDto.api
user_auth = authDto.user_auth


@api.route('/login')
class StaffLogin(Resource):
    """
        Staff Login Resource
    """

    @api.doc('staff login')
    @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        post_data = request.json
        return StaffAuth.login_staff(data=post_data)


@api.route('/logout')
class StaffLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a staff')
    def post(self) -> Tuple[Dict[str, str], int]:
        auth_header = request.headers.get('Authorization')
        return StaffAuth.logout_staff(data=auth_header)
