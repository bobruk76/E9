import os

import pytz
from flask import Flask
import redis
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy


def datetimefilter(value, format='%Y-%m-%dT%H:%M'):
    try:
        tz = pytz.timezone('Europe/Moscow')
        utc = pytz.timezone('UTC')
        value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
        local_dt = value.astimezone(tz)
        return local_dt.strftime(format)
    except:
        return None


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

app.jinja_env.filters['datetimefilter'] = datetimefilter

from api import routes