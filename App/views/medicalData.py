from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_login import LoginManager, UserMixin,login_required
from App.models.forms import UserData
from App.controllers.MedDataFunct import create_record
import json
#from App.models.user import User
medicalData_views = Blueprint('medicalData_views', __name__, template_folder='../templates')

@medicalData_views.route('/dataForm', methods=['GET'])
def getData():
    myForm = UserData()
    return render_template('GetuserData.html',myForm=myForm)

@medicalData_views.route('/getData', methods=['POST'])
def PostData():
    myForm = UserData()
    if myForm.validate_on_submit():
        formData=request.form
        create_record(formData["birthID"],formData["firstname"],formData["middlename"],formData["lastname"],formData["birthPlace"],formData["DateOfBirth"],formData["Sex"],formData["Sex"],formData["Condition1"],formData["Condition2"],formData["Condition3"])
        flash('Your information has been recorded!')
        return redirect("/login")
    flash('Error invalid input!')
    #return redirect("/")
    return render_template('GetuserData.html',myForm=myForm)

@medicalData_views.route("/showData", methods=["GET"])
@login_required
def showInfo():
    person = UserRecords.query.filter_by(birthID=current_identity.id).all()
    person = [data.toDict() for data in person]
    return json.dumps(person) 

