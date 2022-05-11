"""Flaskmin project authenticate admin views"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for

from app.models import Admin
from app.forms import LoginForm, SignUpForm


mod = Blueprint('auth', __name__, url_prefix='/auth')


@mod.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    return render_template('auth/signup.html', form=form)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
