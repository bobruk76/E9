from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class UrlForm(FlaskForm):
    url = TextAreaField(u'Адрес сайта')


class CreateUserForm(FlaskForm):
    name = TextAreaField(u'Имя пользователя')
    email = TextAreaField(u'Почтовый ящик')
    password = TextAreaField(u'Пароль')


class LoginForm(FlaskForm):
    email = TextAreaField(u'Почтовый ящик')
    password = TextAreaField(u'Пароль')
