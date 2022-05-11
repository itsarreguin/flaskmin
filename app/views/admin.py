"""All views for administrate users"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user


mod = Blueprint('admin', __name__)


@mod.route('/dashboard/')
def home():
    return 'Home page'


@mod.route('/employee/add/')
def new_user():
    pass


@mod.route('/logout/')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))
