from flask import Blueprint, render_template


mod = Blueprint('errors', __name__)


@mod.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@mod.app_errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)