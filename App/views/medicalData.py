from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
from App.views.api import LoginManager, UserMixin,login_required,current_user
from App.models.forms import UserData
from App.models.medicalRecords import UserRecords
from App.models.user import User
from App.controllers.MedDataFunct import create_record
import json
#from App.models.user import User
medicalData_views = Blueprint('medicalData_views', __name__, template_folder='../templates')

@medicalData_views.route('/dataForm', methods=['GET'])
def getData():
    myForm = UserData()
    return render_template('GetuserData.html',myForm=myForm)

@medicalData_views.route('/getData', methods=['POST'])
@login_required
def PostData():
    myForm = UserData()
    if myForm.validate_on_submit():
        formData=request.form
        
        create_record(formData["birthID"],formData["firstname"],
        formData["middlename"],formData["lastname"],formData["birthPlace"],
        formData["DateOfBirth"],formData["Sex"],formData["Condition1"],
        formData["Condition2"],formData["Condition3"],user_id=current_user.id)
        flash('Your information has been recorded!')
        return redirect("/mainPage")
    flash('Error invalid input!')
    
    return render_template('GetuserData.html',myForm=myForm)


@medicalData_views.route("/showData", methods=['GET'])
@login_required
def showInfo():
    attributes=("BirthID","Firstname","Middlename","Lastname","BirthPlace","DateOfBirth","Sex","Condition1","Condition2","Condition3")
    user = UserRecords.query.filter_by(user_id=current_user.id).first()
    if user is None:
        data=[]
    #print(user['birthID'], user['user_id'])
    data = [medData.toDict() for medData in user]
    return render_template("ShowUserData.html",attributes=attributes,data=data)

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
    