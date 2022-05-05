"""Create forms for Flaskmin project"""

from flask_wtf import Form
from wtforms import (
    StringField, EmailField, PasswordField, SubmitField
)
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignUpForm(Form):
    pass