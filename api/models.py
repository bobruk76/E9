from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    _id = Column(Integer, primary_key=True)
    email = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    password = Column(String, nullable=False)
    authenticated = Column(Boolean, default=False)

    def get_id(self):
        return self._id

    def get_email(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Event(Base):
    __tablename__ = 'event'
    _id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user._id'), nullable=False)
    timestamp_begin = Column(DateTime(), default=datetime.utcnow)
    timestamp_end = Column(DateTime(), nullable=True)

    title = Column(String(300), unique=False, nullable=True)
    description = Column(String(300), unique=False, nullable=True)


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

