#basic python tools
from datetime import datetime
from uuid import uuid4

#flask + utils
from flask import Blueprint, redirect, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename

#custom flask
from soml.app import app, shitpics
from soml.forms import ImageForm

#custom db
from soml.models import ShitPic

#login
from flask_login import login_required, current_user

#pics
from soml.utils import thumbify

upload_shit_mod = Blueprint('upload_shit_mod', __name__, template_folder='templates')

@upload_shit_mod.route('/upload_shit', methods = ['GET', 'POST'])
@login_required
def upload_shit():
	form = ImageForm()
	if form.validate_on_submit():
		image = thumbify(form.image.data)
		filename = shitpics.save(image, None, 'shitpic_' + secure_filename(form.image.data.filename))
		#filename = shitpics.save(form.image.data, None, 'shitpic_' + secure_filename(form.image.data.filename))
		ShitPic.create(uuid = uuid4(), filename = filename, name = form.name.data, creator = current_user.username, date = datetime.now(), user = int(current_user.get_id()) ) 
		return redirect(url_for('index'))
	return render_template('upload_shit.html', form = form )



	