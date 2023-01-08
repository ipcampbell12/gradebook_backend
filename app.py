from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from Resources.teacher import blp as TeacherBlueprint
from Resources.student import blp as StudentBlueprint
from Resources.assessment import blp as AssessmentBlueprint
from Resources.subject import blp as SubjectBlueprint

import Models 
from db import db

#allows you to parse config file
# takes a configurationa and file and creates a new app
def create_app(Config):
    app = Flask(__name__)

    
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app)

    jwt = JWTManager(app)

    

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(TeacherBlueprint)
    api.register_blueprint(StudentBlueprint)
    api.register_blueprint(AssessmentBlueprint)
    api.register_blueprint(SubjectBlueprint)

    return app


