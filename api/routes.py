from flask_login import login_user
from werkzeug.utils import redirect

from api import app, login_manager, bcrypt, db
from flask import Flask, request, render_template, url_for
from api.forms import UrlForm, CreateUserForm, LoginForm
from api.models import User

from api.service import new_url, get_all_results, get_all_tasks


@app.route('/')
def index():
    results = get_all_results()
    return render_template('index.html', results=results)


@app.route('/tasks/')
def list_tasks():
    tasks = get_all_tasks()
    return render_template('tmpl_tasks.html', tasks=tasks)


@app.route('/add-site', methods=['GET','POST'])
def add_site():
    url_form = UrlForm()
    if request.method == 'POST':
        url = request.form.get('url')
        new_url(url)

        return redirect('/')

    return render_template('new_url.html', form=url_form)


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
        user = User(name=name, email=email, password=bcrypt.generate_password_hash(password).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
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
