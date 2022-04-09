from App.models import UserRecords, User
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.user import User
from App.database import db


def create_record(birthID,firstname,middlename,lastname,birthPlace,DateOfBirth,Sex,Condition1,Condition2,Condition3,user_id):
    newrecord= UserRecords(birthID=birthID,firstname=firstname,middlename=middlename,
                            lastname=lastname,birthPlace=birthPlace,DateOfBirth=DateOfBirth,Sex=Sex,
                            Condition1=Condition1,Condition2=Condition2,Condition3=Condition3,user_id=user_id) 
    db.session.add(newrecord)
    db.session.commit()

def update_record(record,birthID,firstname,middlename,lastname,birthPlace,DateOfBirth,Sex,Condition1,Condition2,Condition3,user_id):
    record.birthID=birthID
    record.firstname=firstname
    record.middlename=middlename
    record.lastname=lastname
    record.birthPlace=birthPlace
    record.DateOfBirth=DateOfBirth
    record.Sex=Sex
    record.Condition1=Condition1
    record.Condition2=Condition2
    record.Condition3=Condition3
    record.user_id=user_id
    db.session.add(record)
    db.session.commit()

def get_all_users_json():
    records = UserRecords.query.all()
    if not records:
        return []
    records = [record.toDict() for record in records]
    return users

def get_all_users():
    return UserRecords.query.all()