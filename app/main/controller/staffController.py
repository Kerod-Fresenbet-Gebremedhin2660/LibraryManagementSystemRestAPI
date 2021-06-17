from flask import request, jsonify
from flask_restx import Resource
from ..utilities.dto import staffDto
from ..service.staffService import get_all_staffs, get_staff, get_staff_by_name, new_staff, delete_staff, delete_staff_by_name


api_staff = staffDto.api
_staff = staffDto.staff


@api_staff.route('/')
class staffList(Resource):
    @api_staff.doc('List of Staff')
    @api_staff.marshal_list_with(_staff, envelope='data')
    def get(self):
        """List all registered staff"""
        return get_all_staffs()

    @api_staff.expect(_staff, validate=True)
    @api_staff.response(201, 'Staff successfully loaded')
    @api_staff.doc('Add a new staff')
    def post(self):
        """create a staff"""
        data = request.json
        return new_staff(data)


@api_staff.route('/<public_id>')
@api_staff.param('privateId', 'The private id of staff')
@api_staff.response(404, 'staff not found.')
class Staff(Resource):
    @api_staff.doc('get a staff')
    @api_staff.marshal_with(_staff)
    def get(self, publicId):
        staff = get_staff(publicId)
        if not staff:
            api_staff.abort(404)
        else:
            return jsonify(staff)

    @api_staff.doc('delete a staff member')
    @api_staff.marshal_with(_staff)
    def delete(self, publicId):
        if get_staff(publicId):
            return delete_staff(publicId)
        else:
            response_object = {
                'status': '404',
                'message': 'The Staff doesn\'t exist'
            }
            return response_object


@api_staff.route('/<name>')
@api_staff.param('email', 'The email of staff')
@api_staff.response(404, 'staff not found.')
class Staff(Resource):
    @api_staff.doc('get a staff')
    @api_staff.marshal_with(_staff)
    def get(self, staffName):
        staff = get_staff_by_name(staffName)
        if not staff:
            api_staff.abort(404)
        else:
            return staff

    @api_staff.doc('delete a staff member')
    @api_staff.marshal_with(_staff)
    def delete(self, staffName):
        if get_staff_by_name(staffName):
            return delete_staff_by_name(staffName)
        else:
            response_object = {
                'status': '404',
                'message': 'staff doesn\'t exist'
            }
            return response_object
