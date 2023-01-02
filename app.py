from flask import Flask
from flask_smorest import Api
from Resources.teacher import blp as TeacherBlueprint
import Models 
from db import db

#allows you to parse config file
# takes a configurationa and file and creates a new app
def create_app(Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(TeacherBlueprint)

    return app


