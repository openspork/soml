from flask import redirect, request, render_template, url_for, send_from_directory


from soml.app import app
from soml.models import User
from soml.forms import RegisterForm, LoginForm
from soml.utils import get_redirect_target


from flask_login import login_user, logout_user, login_required, current_user
from soml.login_controller import login_manager


@app.route('/')
def index():
	return render_template('index.html', current_user = current_user)



@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		username = current_user.username
	else:
		username = 'not logged in'

	form = LoginForm()
	if form.validate_on_submit():
		user = User.get(User.username == form.username.data)
		login_user(user)

		return redirect(get_redirect_target())

	return render_template('login.html', form = form, username = username)

@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)


@app.route('/home')
@login_required
def home():
	return 'you are ' + current_user.username + ' <a href="/logout">logout</a>'


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return 'logged out'












