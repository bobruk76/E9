import os

import Bcrypt as Bcrypt
from flask import Flask
import redis
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy

# nsq_host = str(os.environ.get("NSQ_HOST", "localhost"))
# nsq_port = int(os.environ.get("NSQ_PORT", 4151))

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
from api import routes