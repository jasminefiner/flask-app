from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    from .main_blueprint import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
