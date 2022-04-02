from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models.forms import SignUp, LogIn
from App.models.user import User
api_views = Blueprint('api_views', __name__, template_folder='../templates')

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

@api_views.route('/', methods=['GET'])
#def get_api_docs():
def signup():
    myForm = SignUp()
    return render_template('signup.html',myForm=myForm)

@api_views.route('/signup', methods=['POST'])
def signupUser():
  myForm=SignUp()
  if myForm.validate_on_submit():
    formData=request.myForm
    create_user(formData["username"],formData["email"],formData["password"])
    #newuser = User(username=formData['username'], email=formData['email'])
    #newuser.set_password(formData['password'])
    #print(newuser['username'], newuser['password'])
    #db.session.add(newuser)
    #db.session.commit()
    flash('Your Account Has Been Created!')
    return redirect(url_for('index.html'))
    #return render_template('index.html')
  flash('Error invalid input!')
  return redirect(url_for("signup.html"))
  #return redirect(url_for('sign_up.html')) 

@api_views.route('/login', methods=['GET'])
def getLogin():
  myForm=LogIn()
  return render_template('login.html', myForm=myForm)


@api_views.route('/loginUser', methods=['POST'])
def loginAction():
  myForm = LogIn()
  if myForm.validate_on_submit(): 
      data = request.myForm
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']):
        flash('You have Logged in successfully.')
        login_user(user) 
        return redirect(url_for('https://info-2602-project.dopeskittles.repl.co/'))
  flash('Invalid credentials')
  return redirect(url_for('https://info-2602-project.dopeskittles.repl.co/login.html'))

  