#basic python tools
from datetime import datetime
from uuid import uuid4
import shutil
from io import BytesIO

#HTTP requests
import requests

#flask + utils
from flask import Blueprint, flash, redirect, render_template, send_from_directory, url_for
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
	form.validate_on_submit()
	if form.validate_on_submit():
		try:
			if form.image_upload.data:
				form.image_upload.data.stream = thumbify(form.image_upload.data)[0]
				filename = shitpics.save(form.image_upload.data, None, 'shitpic_' + secure_filename(form.image_upload.data.filename))
				ShitPic.create(uuid = uuid4(), filename = filename, name = form.image_name.data, creator = current_user.username, date = datetime.now(), user = int(current_user.get_id()) )
				return redirect(url_for('index'))
			elif form.image_url.data:
				#url_valid = validate_image_url(form.image_url.data)
				#if url_valid[0]:
				response = requests.get(form.image_url.data, allow_redirects=True)
				content_disposition = response.headers.get('content-disposition')

				thumb_tuple = thumbify(BytesIO(response.content))
				thumb = thumb_tuple[0]
				img_format = thumb_tuple[1]

				if content_disposition:
					image_name = content_disposition
				else:
					image_name = form.image_url.data.rsplit('/', 1)[1] + '.' + img_format

				filename = 'shitpic_' + secure_filename(image_name)

				with open(app.config['UPLOADED_SHITPICS_DEST'] + '/' + filename, 'wb') as out_file:
					shutil.copyfileobj(thumb, out_file)
				del response

				ShitPic.create(uuid = uuid4(), filename = filename, name = form.image_name.data, creator = current_user.username, date = datetime.now(), user = int(current_user.get_id()) )
				return redirect(url_for('index'))

				# else:
				# 	raise Exception(url_valid[1])
		except Exception, e:
			flash (str(e))
	else:
		for field, errors in form.errors.items():
			for error in errors:
				flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error))

		return render_template('upload_shit.html', form = form)

	return render_template('upload_shit.html', form = form)



	