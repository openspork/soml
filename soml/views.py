from flask import redirect, request, render_template, url_for, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user

from soml.login_controller import login_manager
from soml.app import app

from soml.models import *

import os

from uuid import uuid4

#blueprints
from upload_shit.routes import upload_shit_mod
app.register_blueprint(upload_shit_mod)

from login.routes import login_mod
app.register_blueprint(login_mod)

@app.route('/')
def index(alert = None):
	shitpics = ShitPic.select().order_by(ShitPic.score.desc())

	token = Token.create(uuid = uuid4())

	return render_template('index.html', current_user = current_user, shitpics = shitpics, token = token, alert = alert )

@app.route('/shitpic/<op>/<shitpic_uuid>/<token_uuid>')
@login_required
def shitpic_vote(op,shitpic_uuid,token_uuid):
	#check if the token is valid

	sq = Token.select().where(Token.uuid == token_uuid)
	if sq.exists():
		token = Token.get(Token.uuid == token_uuid)
		token.delete_instance()

		shitpic = ShitPic.get(ShitPic.uuid == shitpic_uuid)
	
		if op == 'up':
			shitpic.score += 1
		else:
			shitpic.score -= 1
		shitpic.save()
		return redirect(url_for('index'))
	else:
		alert = 'bad token!'
		return index(alert)


@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html', current_user = current_user)


@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')





