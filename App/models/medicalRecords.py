from App.database import db
from App.models.user import User

class UserRecords(db.Model):
    birthID = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=False)
    birthPlace= db.Column(db.String(120), nullable=False)
    DateOfBirth=db.Column(db.String(20), nullable=False)
    Sex= db.Column(db.String(20), nullable=False)
    Condition1=db.Column(db.String(50), nullable=True)
    Condition2=db.Column(db.String(50), nullable=True)
    Condition3=db.Column(db.String(50), nullable=True)
    user_id= db.Column(db.String(120), db.ForeignKey(User.id))

    def __init__(self,birthID,firstname,middlename,lastname, 
                birthPlace,DateOfBirth,Sex,Condition1,Condition2,Condition3,user_id):
        self.birthID=birthID
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.birthPlace=birthPlace
        self.DateOfBirth=DateOfBirth
        self.Sex=Sex
        self.Condition1=Condition1
        self.Condition2=Condition2
        self.Condition3=Condition3
        self.user_id=user_id

    def toDict(self):
        return{
            'birthID':self.birthID,
            'firstname':self.firstname,
            'middlename':self.middlename,
            'lastname':self.lastname,
            'birthPlace':self.birthPlace,
            'DateOfBirth':self.DateOfBirth,
            'Sex':self.Sex,
            'Condition1':self.Condition1,
            'Condition2':self.Condition2,
            'Condition3':self.Condition3,
            'user_id':self.user_id
        }