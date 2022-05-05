"""All views for administrate users"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for


mod = Blueprint('admin', __name__)


@mod.route('/home/')
def home():
    return 'Home page'


@mod.route('/new/user/')
def new_user():
    pass