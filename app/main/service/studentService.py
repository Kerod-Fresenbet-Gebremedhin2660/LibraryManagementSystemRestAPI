import uuid
import datetime
from app.main import db
from app.main.model.student import Student


def new_student(data):
    student = Student.query.filter_by(email=data['email']).first()
    if not student:
        newStudent = Student(
            studentId=str(uuid.uuid4()),
            studentName=data['studentName'],
            email=data['email'],
            sex=data['sex'],
            dateofBirth=data['dateofBirth'],
            department=data['department'],
            registered_on=str(datetime.datetime.utcnow()),
            password_hash=data['password_hash']
        )
        save_changes(newStudent)
        response_object = {
            'status': 'Success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Email or supplied password is not correct!',
        }
        return response_object, 409


def update_student(data):
    student = get_user_by_name(data['studentName'])
    if student:
        student.studentId = str(student.studentId)
        student.studentName = data['studentName']
        student.email = data['email']
        student.sex = data['sex']
        student.dateofBirth = data['dateofBirth']
        student.department = data['department']
        student.registered_on = str(student.registered_on)
        student.password_hash = data['password_hash']

        save_changes(student)
        response_object = {
            'status': 'Success',
            'message': 'Successfully updated.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'updated failed',
        }
        return response_object, 409


def get_all_users():
    return Student.query.all()


def get_user(studentId):
    return Student.query.filter_by(studentId=studentId).first()


def get_user_by_name(studentName):
    return Student.query.filter_by(studentName=studentName).first()


def delete_user(name):
    student = get_user_by_name(name)
    return student.delete_from_db()


def delete_user_id(public_id):
    student = get_user(public_id)
    return student.delete_from_db()


def delete_user_name(name):
    student = get_user_by_name(name)
    return student.delete_from_db()


def generate_token(student: Student):
    try:
        token = Student.token_encode(Student.studentId)
        response = {
            'status': 'Success',
            'message': 'Registered',
            'authorization': token.decode()
        }
        return response, 201
    except Exception as e:
        response = {
            'status': 'failure',
            'message': 'error'
        }


def save_changes(data):
    db.session.add(data)
    db.session.commit()
