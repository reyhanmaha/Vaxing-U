from App.models import UserRecords
from App.database import db

def create_record(birthID,firstname,middlename,lastname,birthPlace,DateOfBirth,Sex,Condition1,Condition2,Condition3,user_id):
    newrecord= UserRecords(birthID=birthID,firstname=firstname,middlename=middlename,lastname=lastname,birthPlace=birthPlace,DateOfBirth=DateOfBirth,Sex=Sex,Condition1=Condition1,Condition2=Condition2,Condition3=Condition3,user_id=user_id)    
    print(newrecord["birthID"],newrecord["firstname"],newrecord["middlename"],newrecord["lastname"],newrecord["birthPlace"],newrecord["DateOfBirth"],newrecord["Sex"])
    db.session.add(newrecord)
    db.session.commit()

def get_all_users_json():
    records = UserRecords.query.all()
    if not users:
        return []
    records = [record.toDict() for record in records]
    return users

def get_all_users():
    return UserRecords.query.all()