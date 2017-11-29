from flask import redirect, request, render_template, url_for, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user

from soml.login_controller import login_manager
from soml.app import app

from soml.models import *

#blueprints
from upload_shit.routes import upload_shit_mod
app.register_blueprint(upload_shit_mod)

from login.routes import login_mod
app.register_blueprint(login_mod)

@app.route('/')
def index():
	shitpics = ShitPic.select().order_by(ShitPic.score.desc())
	return render_template('index.html', current_user = current_user, shitpics = shitpics )

@app.route('/shitpic/<op>/<uuid>')
@login_required
def shitpic_vote(op,uuid):
	print uuid
	shitpic = ShitPic.get(ShitPic.uuid == uuid)
	if op == 'up':
		shitpic.score += 1
	else:
		shitpic.score -= 1
	shitpic.save()
	return redirect(url_for('index'))






@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html', current_user = current_user)


@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)








