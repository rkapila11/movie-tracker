# Importing the Flask class from flask package
from flask import Flask
import os
# To parse key-value pairs from a local .env file
from dotenv import load_dotenv

# Inject key-value pairs from .env into os.environ dictionary
load_dotenv()

# To create and configure the Flask application instance
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)
    # Retrieve secret key from os.enviorn and assign it to Flask's configuration dictionary
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    return app

