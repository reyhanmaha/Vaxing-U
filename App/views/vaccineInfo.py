from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import LoginManager, UserMixin,login_required,current_user


vaccine_views = Blueprint('vaccine_views', __name__, template_folder='../templates')

@vaccine_views.route('/sinopharm', methods=['GET'])
@login_required
def showSino():
    #myForm = UserData()
    return render_template('sinopharm.html')

@vaccine_views.route('/jj', methods=['GET'])
@login_required
def showJJ():
    #myForm = UserData()
    return render_template('jj.html')

@vaccine_views.route('/astrazeneca', methods=['GET'])
@login_required
def showAstra():
    #myForm = UserData()
    return render_template('astrazeneca.html')

@vaccine_views.route('/pfizer', methods=['GET'])
@login_required
def showPhizer():
    #myForm = UserData()
    return render_template('pfizer.html')