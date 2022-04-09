from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import LoginManager, UserMixin,login_required,current_user


vaccine_views = Blueprint('vaccine_views', __name__, template_folder='../templates')

@vaccine_views.route('/sinopharm', methods=['GET'])
@login_required
def showVaccine():
    #myForm = UserData()
    return render_template('GetuserData.html')

@vaccine_views.route('/j&j', methods=['GET'])
@login_required
def showVaccine():
    #myForm = UserData()
    return render_template('GetuserData.html')

@vaccine_views.route('/astra', methods=['GET'])
@login_required
def showVaccine():
    #myForm = UserData()
    return render_template('GetuserData.html')

@vaccine_views.route('/phizer', methods=['GET'])
@login_required
def showVaccine():
    #myForm = UserData()
    return render_template('GetuserData.html')