from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from wtforms import StringField,BooleanField,SubmitField

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired(),Length(min=1,max=30)])
    last_name = StringField('Last Name',validators=[DataRequired(),Length(min=1,max=30)])
    email = StringField('Email',validators=[DataRequired(),Length(min=4,max=150),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(min=1,max=20)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=5,max=30),EqualTo('password','Passwords do not Match.')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(min=4,max=150),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    submit = SubmitField('Login')
