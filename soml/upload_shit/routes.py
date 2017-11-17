
from flask import Blueprint, redirect, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename

from soml.app import app, shitpics
from soml.forms import ImageForm

mod = Blueprint('upload_shit', __name__, template_folder='templates')

@mod.route('/upload_shit', methods = ['GET', 'POST'])
def upload_shit():
	form = ImageForm()
	if form.validate_on_submit():

		filename = shitpics.save(form.image.data, None, 'test' + secure_filename(form.image.data.filename))
		print 'new pic url', shitpics.url(filename)
		

		return redirect(url_for('index'))
	return render_template('upload_shit.html', form = form )



	