"""Core of Flaskmin project"""

from flask import Flask
from app.config import DevConfig


def main_core():
    app = Flask(__name__)

    app.config.from_object(DevConfig)


    """Register all project blueprints to access routes"""
    from app.views import main
    app.register_blueprint(main.mod)
    
    from app.views import auth
    app.register_blueprint(auth.mod)
    
    from app.views import admin
    app.register_blueprint(admin.mod)


    return app