from flask import Flask
from flask_smorest import Api

from db import db

#allows you to parse config file
# takes a configurationa and file and creates a new app
def create_app(Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    api = Api(app)

    return app


