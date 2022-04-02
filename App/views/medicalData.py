from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models.forms import UserData
#from App.models.user import User
medicalData_views = Blueprint('medicalData_views', __name__, template_folder='../templates')

@medicalData_views.route('/dataForm', methods=['GET'])
#def get_api_docs():
def getData():
    myForm = UserData()
    return render_template('GetuserData.html',myForm=myForm)

@medicalData_views.route('/getData', methods=['POST'])
#def get_api_docs():
def PostData():
    myForm = UserData()
    return render_template('GetuserData.html',myForm=myForm)