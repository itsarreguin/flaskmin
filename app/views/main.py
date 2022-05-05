"""Flaskmin project main views"""

from flask import Blueprint
from flask import render_template, redirect, url_for


mod = Blueprint('main', __name__)


@mod.route('/')
def index():
    return render_template('main/index.html')