from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.forms import MakeBooking
from App.models.booking import Appointments
from App.controllers.bookingOps import create_appointment
import json
#from App.models.user import User
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
        create_appointment(bookingData["vaccineLoc"],bookingData["vaccineType"],bookingData["date"],bookingData["time"],bookingData["user_id"])
        return redirect("/mainPage")
    flash('Error invalid input!')
    #return redirect("/")
    return redirect("/mainPage")