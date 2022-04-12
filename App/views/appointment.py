from flask import Blueprint, redirect, render_template, request, send_from_directory, flash, url_for
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.forms import MakeBooking
from App.models.booking import Appointments
from App.controllers.bookingOps import create_appointment, cancel_all_bookings
from App.database import db
import json

booking_views = Blueprint('booking_views', __name__, template_folder='../templates')

@booking_views.route('/booking', methods=['GET'])
@login_required
def getData():
    myForm = MakeBooking()
    return render_template('bookingPage.html',myForm=myForm)

@booking_views.route('/getBooking', methods=['POST'])
@login_required
def PostData():
    myForm = MakeBooking()
    if myForm.validate_on_submit():
        bookingData=request.form
        create_appointment(bookingData["vaccineLoc"],bookingData["vaccineType"],bookingData["date"],bookingData["time"],user_id=current_user.id)
        return redirect(url_for('mainPage_views.show_main'))
    flash('Error invalid input!')
    return redirect(url_for('mainPage_views.show_main'))

@booking_views.route('/cancelBookings', methods=['GET'])
@login_required
def cancel_bookings():
    bookings=Appointments.query.filter_by(bookingID=current_user.id).all()
    if bookings:
        cancel_all_bookings(bookings)
        return redirect(url_for('mainPage_views.show_main'))
    return redirect(url_for('mainPage_views.show_main'))
