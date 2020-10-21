from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, PasswordField, validators


class EventForm(FlaskForm):
    title = StringField(u'Заголовок события')
    description = TextAreaField(u'Описание события')

    timestamp_begin = DateTimeField(u'Время начала события')
    timestamp_end = DateTimeField(u'Время конца события')


class CreateUserForm(FlaskForm):
    name = StringField(u'Имя пользователя', [validators.Length(min=6, max=35)])
    email = StringField(u'Почтовый ящик', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField(u'Повторите пароль')


class LoginForm(FlaskForm):
    email = TextAreaField(u'Почтовый ящик')
    password = TextAreaField(u'Пароль')
