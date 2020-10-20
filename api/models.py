import enum
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


class Task(Base):
    __tablename__ = 'task'
    _id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user._id'), nullable=False)
    timestamp_begin = Column(DateTime(), default=datetime.utcnow)
    timestamp_end = Column(DateTime(), nullable=True)

    address = Column(String(300), unique=False, nullable=True)

    task_stat = Column(Integer, default=1)
    # task_status = Column(Enum(TaskStatus), default=TaskStatus.NOT_STARTED)
    http_status = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

