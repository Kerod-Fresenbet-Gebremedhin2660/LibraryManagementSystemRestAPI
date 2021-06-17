from app.main.model.student import Student
from app.main.model.staff import Staff
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            student = Student.query.filter_by(email=data.email).first()
            if student and student.check_password(data.password_hash):
                auth_token = student.token_encode(student.studentId)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Student.token_decode(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Student.token_decode(auth_token)
            if not isinstance(resp, str):
                student = Student.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'student_id': student.studentId,
                        'student_email': student.email,
                        'registered_on': str(student.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401


##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################

class StaffAuth:
    @staticmethod
    def login_staff(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            staff = Staff.query.filter_by(email=data.get('email')).first()
            if staff and staff.check_password(data.get('password')):
                auth_token = staff.encode_auth_token(staff.staffId)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_staff(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Staff.token_decode(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Staff.token_decode(auth_token)
            if not isinstance(resp, str):
                staff = Staff.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'staff_id': staff.studentId,
                        'student_email': staff.email,
                        'registered_on': str(staff.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
