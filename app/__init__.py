from flask import Flask

app = Flask(__name__)

# This import is at the bottom of the file to prevent a circular import
# situation with flask.
from app import routes
