from flask import flash, redirect, request, render_template, url_for, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user

from soml.login_controller import login_manager
from soml.app import app
from soml.models import ShitPic

import os

from uuid import uuid4

#blueprints
from upload_shit.routes import upload_shit_mod
app.register_blueprint(upload_shit_mod)

from login.routes import login_mod
app.register_blueprint(login_mod)

from profile.routes import profile_mod
app.register_blueprint(profile_mod)

from index.routes import index_mod
app.register_blueprint(index_mod)

@app.route('/shitpic/get/<uuid>')
def shitpic_get(uuid):
	directory = app.config['UPLOADED_SHITPICS_DEST']
	filename = ShitPic.get(ShitPic.uuid == uuid).filename
	print 'serving picture ', directory + filename
	return send_from_directory(directory, filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')





