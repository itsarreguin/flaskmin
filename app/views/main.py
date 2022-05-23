"""Flaskmin project main views"""

from flask import Blueprint
from flask import render_template, redirect, url_for


mod = Blueprint('main', __name__)


@mod.route('/')
def index():
    return render_template('main/index.html')


@mod.route('/login/')
def login_redirect():
    return redirect(url_for('auth.login'))


@mod.route('/signup/')
def signup_redirect():
    return redirect(url_for('auth.signup'))