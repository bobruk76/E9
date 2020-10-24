from api import db, bcrypt
from sqlalchemy.orm import sessionmaker

from api.models import Event, User


def new_event(user, title, description, timestamp_begin, timestamp_end):
    new_task = Event(address=url)
    db.session.add(new_task)
    db.session.commit()


def get_all_events():
    return db.session.query(Event).all()


def get_user(name):
    return db.session.query(User).filter(User.name == name).one_or_none()


def get_user_by_id(id):
    return db.session.query(User).filter(User._id == id).one_or_none()


def get_all_users():
    return db.session.query(User).all()


def new_user(name, email, password):
    user = User(name=name, email=email, password=bcrypt.generate_password_hash(password).decode('utf-8'))
    db.session.add(user)
    db.session.commit()
    return user





