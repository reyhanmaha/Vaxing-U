from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from App.models.forms import UserData
from App.controllers.MedDataFunct import create_record
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
        create_record(formData["birthID"],formData["firstname"],formData["middlename"],formData["lastname"],formData["birthPlace"],formData["DateOfBirth"],formData["Sex"],formData["Sex"])
        flash('Your information has been recorded!')
        return redirect("/mainPage")
    flash('Error invalid input!')
    #return redirect("/")
    return render_template('GetuserData.html',myForm=myForm)