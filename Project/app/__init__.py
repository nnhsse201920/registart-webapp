from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

from app import routes