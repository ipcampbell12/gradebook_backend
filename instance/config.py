import os
from dotenv import load_dotenv



# path to current file
# basedir = path.abspath(path.dirname(__file__))

# loads variable data stored in .env file



class Config: 
    
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Stores REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH= "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    JWT_SECRET_KEY = "209464218638121439204640626213139170704"

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


        