from App.database import db
from App.models.user import User

class UserRecords(db.Model):
    birthID = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    birthPlace= db.Column(db.String(120), nullable=False)
    #DateOfBirth=db.Column(db.)
    Sex= db.Column(db.String(20), nullable=False)
    user_id= db.Column(db.String(100), db.ForeignKey('user_id'))

    def __init__(self,id,username,email,password):
        self.id=id
        self.username=username
        self.email=email
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'password': self.password
        }