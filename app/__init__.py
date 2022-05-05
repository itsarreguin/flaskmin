from flask import Flask
from app.config import DevConfig


"""Core of flask project"""
def main_core():
    app = Flask(__name__)
    
    app.config.from_object(DevConfig)


    """Register all project blueprints to access routes"""
    from app.views import main
    app.register_blueprint(main.mod)


    return app