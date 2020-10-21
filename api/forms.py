from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField


class EventForm(FlaskForm):
    title = StringField(u'Заголовок события')
    description = TextAreaField(u'Описание события')

    timestamp_begin = DateTimeField(u'Время начала события')
    timestamp_end = DateTimeField(u'Время конца события')


class CreateUserForm(FlaskForm):
    name = TextAreaField(u'Имя пользователя')
    email = TextAreaField(u'Почтовый ящик')
    password = TextAreaField(u'Пароль')


class LoginForm(FlaskForm):
    email = TextAreaField(u'Почтовый ящик')
    password = TextAreaField(u'Пароль')
