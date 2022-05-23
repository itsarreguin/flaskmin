"""Core of Flaskmin project"""

from flask import Flask
from flask_login import LoginManager

from app.config import DevConfig
from db.settings import db_session


login_manager = LoginManager()


def main_core():
    app = Flask(__name__)

    app.config.from_object(DevConfig)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    """Register all project blueprints to access routes"""
    from app.views import main
    app.register_blueprint(main.mod)

    from app.views import admin
    app.register_blueprint(admin.mod)

    from app.views import auth
    app.register_blueprint(auth.mod)
    
    from app.views import errors
    app.register_blueprint(errors.mod)


    return app


app = main_core()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()