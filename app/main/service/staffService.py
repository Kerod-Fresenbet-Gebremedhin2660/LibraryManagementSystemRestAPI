import uuid
import datetime
from app.main import db
from app.main.model.staff import Staff


def new_staff(data):
    staff = Staff.query.filter_by(staffId=data['staffId']).first()
    if not staff:
        newstaff = staff(
            staffId=uuid.uuid4(),
            staffName=data['staffName'],
            email=data['email'],
            registered_on=datetime.datetime.utcnow(),
            password=data['password']
        )
        save_changes(newstaff)
        response_object = {
            'status': 'success',
            'message': 'Successfully Registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'staff already in the system',
        }
        return response_object, 409


def update_staff(data):
    staff = Staff.query.filter_by(isbn=data['staffId']).first()
    if not staff:
        newstaff = staff(
            staffName=data['staffName'],
            email=data['email'],
            registered_on=datetime.datetime.utcnow(),
            password=data['password']
        )
        save_changes(newstaff)
        response_object = {
            'status': 'success',
            'message': 'Successfully Registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'staff already in the system',
        }
        return response_object, 409


def delete_staff(staffId):
    staff = get_staff(staffId)
    return staff.delete_from_db()


def delete_staff_by_name(staffName):
    return Staff.find_by_name(staffName)


def get_all_staffs():
    return Staff.query.all()


def get_staff(staffId):
    return Staff.query.filter_by(staffId=staffId).first()


def get_staff_by_name(studentName):
    return Staff.query.filter_by(studentName=studentName).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
