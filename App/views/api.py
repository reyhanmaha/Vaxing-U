from flask import Blueprint, redirect, render_template, request, send_from_directory, flash, url_for
from flask_login import LoginManager, UserMixin
#from flask_jwt import jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from App.models.forms import SignUp, LogIn
from App.models.user import User
from App.controllers import *
from App.controllers.auth import login_user, authenticate, identity, setup_jwt
#from App.main import login_manager

api_views = Blueprint('api_views', __name__, template_folder='../templates')

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)
#login_manager=LoginManager()
#login_manager.init_app(app)


@api_views.route('/', methods=['GET'])
#def get_api_docs():
def signup():
    myForm = SignUp()
    return render_template('signup.html',myForm=myForm)

@api_views.route('/signup', methods=['POST'])
def signupUser():
  form=SignUp()
  if form.validate_on_submit():
    formData=request.form
    create_user(formData["username"],formData["email"],formData["password"])
    flash('Your Account Has Been Created!')
    #return redirect(url_for('/templates/GetuserData.html'))
    return redirect("/dataForm")
  flash('Error invalid input!')
  return redirect(url_for("signup.html"))

#@login_manager.user_loader

@api_views.route('/login', methods=['GET'])
def getLogin():
  myForm=LogIn()
  return render_template('login.html', myForm=myForm)


@api_views.route('/loginUser', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit():
      data = request.form
      user = authenticate(data["username"],data["password"])#User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']):
        login_user(user,remember=False)
        flash('You have Logged in successfully.')
        return redirect("/mainPage")
      flash('Invalid credentials')
      myForm=LogIn()
      return render_template('login.html',myForm=myForm)

  