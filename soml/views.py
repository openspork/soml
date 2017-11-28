from flask import redirect, request, render_template, url_for, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user

from soml.login_controller import login_manager
from soml.app import app


@app.route('/')
def index():
	return render_template('index.html', current_user = current_user)


@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)


@app.route('/home')
@login_required
def home():
	return 'you are ' + current_user.username + ' <a href="/logout">logout</a>'





