from flask_login import login_user
from werkzeug.utils import redirect

from api import app, login_manager, bcrypt, db
from flask import Flask, request, render_template
from api.forms import CreateUserForm, LoginForm, EventForm
from api.models import User

from api.service import get_all_events, new_user


@app.route('/')
def index():
    results = get_all_events()
    return render_template('index.html', results=results)


@app.route('/event/')
def list_events():
    events = get_all_events()
    return render_template('list_events.html', evenvts=events)


@app.route('/event/new', methods=['GET', 'POST'])
def add_site():
    event_form = EventForm()
    if request.method == 'POST':
        url = request.form.get('url')
        new_url(url)

        return redirect('/')

    return render_template('new_url.html', form=event_form)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        new_user(name, email, password)
        return redirect("/")
    return render_template("login.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect("/")
    return render_template("login.html", form=form)
