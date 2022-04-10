from App.database import db
from App.models.user import User
from sqlalchemy.dialects.postgresql import UUID

class Appointments(db.Model):
    bookingID=db.Column(db.String(120), primary_key=True)
    vaccineLoc= db.Column(db.String(100), nullable=False)
    vaccineType=db.Column(db.String(100), nullable=False)
    date=db.Column(db.String(100), nullable=False)
    time=db.Column(db.String(100),unique=True, nullable=False)
    user_id= db.Column(db.String(120), db.ForeignKey(User.id))

    def __init__(self,bookingID,vaccineLoc,vaccineType,date,time,user_id):
        self.bookingID=bookingID
        self.vaccineLoc=vaccineLoc
        self.vaccineType=vaccineType
        self.date=date
        self.time=time
        self.user_id=user_id

    def toDict(self):
        return{
            'bookingID':self.bookingID,
            'vaccineLoc':self.vaccineLoc,
            'vaccineType':self.vaccineType,
            'date':self.date,
            'time':self.time,
            'user_id':self.user_id
        }