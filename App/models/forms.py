from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms import DateField

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = StringField('email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class MakeBooking(FlaskForm):
    vaccineLoc= StringField('vaccineLoc', validators=[InputRequired()])
    vaccineType= StringField('vaccineType', validators=[InputRequired()])
    date= StringField('date', validators=[InputRequired()])
    time= StringField('time', validators=[InputRequired()])
    submit= SubmitField('Book Appointment', render_kw={'class': 'btn waves-effect waves-light white-text'})


class UserData(FlaskForm):
    birthID=IntegerField('birthID', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    middlename = StringField('middlename')
    lastname = StringField('lastname', validators=[InputRequired()])
    birthPlace = StringField('birthPlace', validators=[InputRequired()])
    #DateOfBirth = DateField('DateOfBirth',format='%d-%m-%Y', validators=[InputRequired()])
    DateOfBirth = StringField('DateOfBirth', validators=[InputRequired()])
    Sex = StringField('Sex', validators=[InputRequired()])
    Condition1=StringField('Condition1')
    Condition2=StringField('Condition2')
    Condition3=StringField('Condition3')
    submit = SubmitField('Submit', render_kw={'class': 'btn waves-effect waves-light white-text'})