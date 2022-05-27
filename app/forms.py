"""Create forms for Flaskmin project"""

from flask_wtf import Form, FlaskForm
from wtforms.fields import (
    StringField, EmailField, PasswordField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=4, max=25)]
        )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=10, max=20)]
        )
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    first_name = StringField(
        'First name', validators=[DataRequired(), Length(min=1, max=25)]
        )
    last_name = StringField(
        'Last name', validators=[DataRequired(), Length(min=1, max=25)]
        )
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=1, max=20)]
        )
    email = EmailField(
        'Your e-mail address', validators=[DataRequired(), Length(min=8, max=60)]
        )
    password_hash = PasswordField('Create a password',
        validators=[
            DataRequired(), Length(min=10, max=20),
            EqualTo('password_verify', message='Passwords do not match')
            ]
        )
    password_verify = PasswordField(
        'Confirm your password', validators=[DataRequired(), Length(min=10, max=20)]
    )
    submit = SubmitField('Register')


class AdminProfile(Form):
    pass


class EmployeeForm(FlaskForm):
    first_name = StringField(
        'First name', validators=[DataRequired(), Length(min=1, max=25)]
        )
    last_name = StringField(
        'Last name', validators=[DataRequired(), Length(min=1, max=25)]
        )
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=1, max=20)]
        )
    email = StringField(
        'Email address', validators=[DataRequired(), Length(min=8, max=60)]
        )
    create = SubmitField('Add employee')
    update = SubmitField('Update information')