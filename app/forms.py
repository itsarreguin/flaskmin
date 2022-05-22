"""Create forms for Flaskmin project"""

from flask_wtf import Form, FlaskForm
from wtforms import (
    StringField, EmailField, PasswordField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Second name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Your e-mail address', validators=[DataRequired()])
    password_hash = PasswordField('Create a password',
        validators=[DataRequired(), EqualTo('password_verify', message='Passwords do not match')])
    password_verify = PasswordField(
        'Confirm your password', validators=[DataRequired()]
    )
    submit = SubmitField('Register')


class AdminProfile(Form):
    pass


class EmployeeForm(Form):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    submit = SubmitField(label='Add employee')
