import os 
import secrets

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
# from instance.config import Config, ProdConfig
# import instance.config


from db import db
from instance.blocklist import BLOCKLIST
import Models 

from Resources.teacher import blp as TeacherBlueprint
from Resources.student import blp as StudentBlueprint
from Resources.assessment import blp as AssessmentBlueprint
from Resources.subject import blp as SubjectBlueprint



migrate = Migrate()
jwt = JWTManager()
cors = CORS()

#allows you to parse config file
# takes a configurationa and file and creates a new app
def create_app(db_url=None):
    app = Flask(__name__)
    # load_dotenv()
    # app.config.from_object(config)
    

    #need this in order to make data able to be fetched to front end
    
     #configuration variables

    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["API_TITLE"] = "Stores REST API"
    app.config['API_VERSION'] = "v1"
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    #if db_url exists, use that, otherwise, use the next one
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
 
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = '157481405834678672455234309838136777491'

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

    db.create_all()
    return app


app = create_app()




