from api import db, bcrypt
from sqlalchemy.orm import sessionmaker

from api.models import Event, User


def new_event(user_id, title, description, timestamp_begin, timestamp_end):
    _event = Event(user_id=user_id,
                   title=title,
                   description=description,
                   timestamp_begin=timestamp_begin,
                   timestamp_end=timestamp_end)

    db.session.add(_event)
    db.session.commit()
    return _event


def get_all_events():
    records = db.session.query(Event, User).join(User, Event.user_id == User._id).all()
    return records


def get_event_by_id(id):
    return db.session.query(Event).filter(Event._id == id).one_or_none()


def del_event(event_id, user_id):
    db.session.query(Event).filter(Event._id == event_id, Event.user_id == user_id).delete()
    db.session.commit()


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
