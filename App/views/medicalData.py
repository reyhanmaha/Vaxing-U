from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from flask_login import LoginManager, UserMixin,login_required,current_user
from App.models.forms import UserData
from App.models.medicalRecords import UserRecords
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

@medicalData_views.route("/showData", methods=['GET'])
@login_required
def showInfo():
    attributes=("BirthID","Firstname","Middlename","Lastname","BirthPlace","DateOfBirth","Sex","Condition1","Condition2","Condition3")
    user = UserRecords.query.filter_by(user_id=current_user.id).all()
    
    user = [medData.toDict() for medData in user]
    print(user[2],user[1],user[4])
    return render_template("ShowUserData.html",attributes=attributes,user=user)

@medicalData_views.route("/update", methods=['GET'])
@login_required
def getUpdate():
    myForm=UserData()
    render_template("updateData.html",myForm=myForm)


@medicalData_views.route("/updateFile",methods=['POST'])
@login_required
def updateData():
    if myForm.validate_on_submit():
        data=request.form
        record = UserRecords.query.filter_by(user_id=current_user.data["birthID"], birthID=birthID).first()
        if record == None:
            return 'Invalid birthID'
        #data = request.get_json()
            if 'name' in data:
                record.name = data['name']
                db.session.add(record)
                db.session.commit()
                return 'Updated', 201
    