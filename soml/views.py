from flask import render_template, send_from_directory
from app import app

from soml.models import User

from flask_login import LoginManager, login_user, logout_user, login_required, current_user


#login settings
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return User.get(User.id == int(user_id))





@app.route('/')
def index():
	return render_template('index.html')

@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)


@app.route('/login')
def login():
	user = User.get(User.username == 'christian')
	login_user(user)
	print 'logging in', user.username
	return 'logged in'

@login_required
@app.route('/home')
def home():
	return 'you are ' + current_user.username

@login_required
@app.route('/logout')
def logout():
	logout_user()
	return 'logged out'












