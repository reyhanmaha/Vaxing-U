from App.models import User
from App.database import db
import uuid

def get_all_users():
    return User.query.all()


def create_user(username,email, password):
    newuser =User(id=str(uuid.uuid4()),username=username,email=email,password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()