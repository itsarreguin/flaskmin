"""Create forms for Flaskmin project"""

from flask_wtf import Form
from wtforms import (
    StringField, EmailField, PasswordField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Second name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Your e-mail address', validators=[DataRequired()])
    password_hash = PasswordField(
        'Create a password',
        validators=[DataRequired(), EqualTo('password_hash', message='Passwords do not match')])
    password_verify = PasswordField(
        'Verify your password', validators=[DataRequired()]
    )
    submit = SubmitField('Register')


class AdminProfile(Form):
    pass


class Employee(Form):
    pass
