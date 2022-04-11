from flask import Blueprint, redirect, render_template, request, send_from_directory, flash, url_for
from App.views.api import LoginManager, UserMixin,login_required,current_user
from App.models.forms import UserData
from App.models.medicalRecords import UserRecords
from App.models.user import User
from App.controllers.MedDataFunct import create_record, update_record
import json

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
        #return redirect("/mainPage")
        return redirect(url_for('mainPage_views.show_main'))
    flash('Error invalid input!')
    return render_template('GetuserData.html',myForm=myForm)


@medicalData_views.route("/showData", methods=['GET'])
@login_required
def showInfo():
    record = UserRecords.query.filter_by(user_id=current_user.id).first()
    if record is None:
        data=[]
    data=record.toDict()
    return render_template("ShowUserData.html",data=data)

@medicalData_views.route("/update", methods=['GET'])
@login_required
def getUpdate():
    myForm=UserData()
    return render_template("updateData.html",myForm=myForm)


@medicalData_views.route("/updateFile",methods=['POST'])
@login_required
def updateData():
    myForm=UserData()
    if myForm.validate_on_submit():
        data=request.form
        record = UserRecords.query.filter_by(user_id=current_user.id).first()
        if record == None:
            #return redirect("/mainPage")
            return redirect(url_for('mainPage_views.show_main'))
        update_record(record,data["birthID"],data["firstname"],data["middlename"],data["lastname"],
                        data["birthPlace"],data["DateOfBirth"],data["Sex"],
                        data["Condition1"],data["Condition2"],data["Condition3"],user_id=current_user.id)
        #return redirect("/showData")
        return redirect(url_for('medicalData_views.showInfo'))
        
