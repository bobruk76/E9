from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from wtforms.ext.appengine.db import model_form

from api import app, login_manager, bcrypt, db
from flask import Flask, request, render_template, flash, session
from api.forms import CreateUserForm, LoginForm, EventForm
from api.models import User, Event

from api.service import get_all_events, new_user, new_event, get_all_users, get_user, get_user_by_id, del_event, \
    get_event_by_id


@app.route('/')
def index():
    results = get_all_events()
    return render_template('index.html', results=results)


@app.route('/event/')
def list_events():
    if current_user.is_authenticated:
        current_user_id = current_user.get_id()

        events = get_all_events()
        return render_template('list_events.html', data=events, current_user_id=current_user_id)
    return redirect('/')


@app.route('/event/<event_id>/del', methods=['GET', 'POST', 'PUT', ])
def event_del(event_id):
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        del_event(event_id, user_id)
        return redirect('/event/')
    return redirect('/')


@app.route('/event/<event_id>', methods=['GET', 'POST'])
def event_actions(event_id):
    def date_check(_datetime):
        if _datetime == '':
            return None
        return _datetime

    if current_user.is_authenticated:
        _event = None
        if event_id.isnumeric():
            _event = get_event_by_id(int(event_id))
            event_form = EventForm(obj=_event)
        else:
            event_form = EventForm()

        if request.method == 'POST':

            title = request.form.get('title')
            description = request.form.get('description')

            timestamp_begin = date_check(request.form.get('timestamp_begin'))
            timestamp_end = date_check(request.form.get('timestamp_end'))
            user_id = current_user.get_id()
            if _event:

                _event = \
                    new_event(user_id=user_id,
                              title=title,
                              description=description,
                              timestamp_begin=timestamp_begin,
                              timestamp_end=timestamp_end)
            else:
                _event = \
                    new_event(user_id=user_id,
                              title=title,
                              description=description,
                              timestamp_begin=timestamp_begin,
                              timestamp_end=timestamp_end)

            return redirect('/event/')
        return render_template('edit_event.html', form=event_form)
    flash("Только зарегистрированный пользователь может добавлять событие")
    return redirect('/')


@login_manager.user_loader
def user_loader(user_id):
    return get_user_by_id(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.name.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect("/")
            else:
                flash("Неверное имя пользователя или пароль")
    return render_template("login_user.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']
    flash('Вы должны авторизоваться')
    return redirect('/login')


@app.route('/user/')
def list_users():
    users = get_all_users()
    return render_template('list.html', data=users, title=u"Список пользователей")


@app.route("/user/new", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.is_submitted():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not get_user(name):
            user = new_user(name, email, password)
            login_user(user, remember=True)
            return redirect("/event/")
        else:
            flash('Такой пользователь уже существует!')

    return render_template("create_user.html", form=form)
