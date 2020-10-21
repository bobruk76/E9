import os


from flask import Flask
import redis
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
from api import routes