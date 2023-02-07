import os 

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
# from dotenv import load_dotenv
from instance.config import Config


from Resources.teacher import blp as TeacherBlueprint
from Resources.student import blp as StudentBlueprint
from Resources.assessment import blp as AssessmentBlueprint
from Resources.subject import blp as SubjectBlueprint
from instance.blocklist import BLOCKLIST


from db import db
import Models 

#allows you to parse config file
# takes a configurationa and file and creates a new app
def create_app(config):
    app = Flask(__name__)
    # load_dotenv()

    #need this in order to make data able to be fetched to front end
    CORS(app)

    
    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)
    api = Api(app)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload['jti'] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header,jwt_payload):
        return(
            jsonify(
                {"description":"The token has been revoked.","error":"token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description":"The token is not fresh",
                    "error":"fresh_token_required"
                }
            )
        )
    
    @jwt.expired_token_loader
    def expired_token_laoder(jwt_header, jwt_payload):

        return (
            jsonify({"message":"The token has expired.","error":"token_expired"},401,)
        )

    @jwt.invalid_token_loader
    def invalied_token_callback(error):
        return (
            jsonify(
                {"message":"Signature verification failed.","error":"invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description":"Request does not contain acces token.",
                    "error":"authorization_required"
                }
            ),
            401,
        )

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    api.register_blueprint(TeacherBlueprint)
    api.register_blueprint(StudentBlueprint)
    api.register_blueprint(AssessmentBlueprint)
    api.register_blueprint(SubjectBlueprint)

    return app




app = create_app(Config)
