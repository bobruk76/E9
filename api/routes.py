from werkzeug.utils import redirect

from api import app
from flask import Flask, request, render_template, url_for
from api.forms import UrlForm

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

