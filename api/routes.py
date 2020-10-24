from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect

from api import app, login_manager, bcrypt, db
from flask import Flask, request, render_template, flash, session
from api.forms import CreateUserForm, LoginForm, EventForm
from api.models import User

from api.service import get_all_events, new_user, new_event, get_all_users, get_user, get_user_by_id


@app.route('/')
def index():
    results = get_all_events()
    return render_template('index.html', results=results)


@app.route('/event/')
def list_events():
    events = get_all_events()
    return render_template('list.html', evenvts=events)


@app.route('/event/new', methods=['GET', 'POST'])
def add_event():
    event_form = EventForm()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        timestamp_begin = request.form.get('timestamp_begin')
        timestamp_end = request.form.get('timestamp_end')
        user_id = current_user.get_id()

        new_event(user_id=user_id,
                      title=title,
                      description=description,
                      timestamp_begin=timestamp_begin,
                      timestamp_end=timestamp_end)

        return redirect('/')

    return render_template('new_url.html', form=event_form)


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
    return render_template("login_user.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    if session.get('was_once_logged_in'):
        # prevent flashing automatically logged out message
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
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
