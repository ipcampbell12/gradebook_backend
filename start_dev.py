from app import create_app
from dotenv import load_dotenv
from instance.config import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True)