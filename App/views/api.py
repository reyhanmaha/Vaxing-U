from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models.forms import SignUp, LogIn
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
  myForm = SignUp()
  if myForm.validate_on_submit():
    data = request.myForm
    newuser = User(username=data['username'], email=data['email'])
    newuser.set_password(data['password'])
    print(newuser['username'], newuser['password'])
    db.session.add(newuser)
    db.session.commit()
    flash('Your Account Has Been Created!')
    return redirect(url_for('index.html'))
    #return render_template('index.html')
  #flash('Error invalid input!')
  #return render_template('sign_up.html', myForm=myForm)
  #return redirect(url_for('sign_up.html')) 

@api_views.route('/login', methods=['GET'])
def getLogin():
  form = LogIn()
  return render_template('login.html', form=form)


@api_views.route('/loginUser', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): 
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']):
        flash('You have Logged in successfully.')
        login_user(user) 
        return redirect(url_for('https://info-2602-project.dopeskittles.repl.co/'))
  flash('Invalid credentials')
  return redirect(url_for('https://info-2602-project.dopeskittles.repl.co/login.html'))

  