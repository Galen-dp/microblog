from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# This import is at the bottom of the file to prevent a circular import
# situation with flask.
from app import routes
