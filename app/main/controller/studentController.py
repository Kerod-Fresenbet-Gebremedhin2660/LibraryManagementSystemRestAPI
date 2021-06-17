from flask import request
from flask_restx import Resource
from ..utilities.dto import studentDto
from ..service.studentService import get_all_users, get_user, new_student, delete_user_id, update_student, \
    get_user_by_name, delete_user_name

api_student = studentDto.api
_student = studentDto.student


@api_student.route('/student')
class StudentList(Resource):
    @api_student.doc('List of Students')
    @api_student.marshal_list_with(_student, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api_student.expect(_student, validate=True)
    @api_student.response(201, 'Student successfully created.')
    @api_student.doc('create a new Student')
    def post(self):
        """Creates a new student"""
        data = request.json
        return new_student(data=data)


@api_student.route('/student/<public_id>')
@api_student.param('public_id', 'The User identifier')
@api_student.response(404, 'User not found.')
class Student(Resource):
    @api_student.doc('get a user')
    @api_student.marshal_with(_student)
    def get(self, public_id):
        """get a student given identifier"""
        user = get_user(public_id)
        if not user:
            api_student.abort(404)
        else:
            return user

    @api_student.doc('delete a user')
    @api_student.marshal_with(_student)
    def delete(self, public_id):
        """delete a student given identifier"""
        if get_user(public_id):
            return delete_user_id(public_id)
        else:
            api_student.abort(404)

    @api_student.doc('update a user')
    @api_student.expect(_student, validate=True)
    @api_student.marshal_with(_student)
    def update(self, public_id):
        """update a student given identifier"""
        data = request.json
        if get_user(public_id):
            return update_student(data)
        else:
            api_student.abort(404)


@api_student.route('/student/<string:name>')
@api_student.param('name', 'The username')
@api_student.response(404, 'User not found.')
class StudentEmail(Resource):
    @api_student.doc('get a user using username')
    @api_student.marshal_with(_student)
    def get(self, name):
        """get a student given username"""
        user = get_user_by_name(name)
        if not user:
            api_student.abort(404)
        else:
            return user

    @api_student.doc('delete a user')
    @api_student.marshal_with(_student)
    def delete(self):
        """delete a student given name"""
        data = request.json
        return delete_user_name(data['studentName'])

    @api_student.doc('update a user')
    @api_student.expect(_student, envelop=True)
    def patch(self):
        """updates a student given name"""
        data = request.json
        user = get_user_by_name(data['studentName'])
        if not data and user:
            api_student.abort(404)
        else:
            return update_student(data)
