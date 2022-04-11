from App.models import Appointments
from App.database import db
import uuid

def create_appointment(vaccineLoc,vaccineType,date,time,user_id):
    newBooking= Appointments(bookingID=str(uuid.uuid4()),vaccineLoc=vaccineLoc,vaccineType=vaccineType,date=date,time=time,user_id=user_id)    
    db.session.add(newBooking)
    db.session.commit()

def cancel_all_bookings(bookings):
    db.session.delete(bookings)
    db.session.commit()

def get_all_users_json():
    bookings = Appointments.query.all()
    if not users:
        return []
    bookings = [booking.toDict() for booking in bookings]
    return bookings

def get_all_users():
    return Appointments.query.all()