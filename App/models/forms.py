from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = StringField('email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()]) #, EqualTo('confirm', message='Passwords must match')])
    #confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class UserData(FlaskForm):
    birthID=IntegerField('birthID', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    middlename = StringField('middlename')
    lastname = StringField('lastname', validators=[InputRequired()])
    birthPlace = StringField('birthPlace', validators=[InputRequired()])
    DateOfBirth = StringField('DateOfBirth', validators=[InputRequired()])
    Sex = StringField('Sex', validators=[InputRequired()])
    submit = SubmitField('Submit', render_kw={'class': 'btn waves-effect waves-light white-text'})