from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class UrlForm(FlaskForm):
    url = TextAreaField(u'Адрес сайта')


