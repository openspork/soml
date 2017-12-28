
from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import login_required, current_user
from soml.forms import ProfileForm
from soml.models import ShitPic

profile_mod = Blueprint('profile_mod', __name__, template_folder='templates')

@profile_mod.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
	choices = []
	for shitpic in current_user.shitpics:
		choices.append((str(shitpic.uuid), shitpic.name))

	form = ProfileForm(choices = choices)
	if form.validate_on_submit():
		print form.delete.data
		for shitpic_uuid in form.delete.data:
			print 'deleting', shitpic_uuid
			ShitPic.get(ShitPic.uuid == shitpic_uuid).delete_instance()
		return redirect(url_for('profile_mod.profile'))

	else:
		for field, errors in form.errors.items():
			for error in errors:
				flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error))

	return render_template('profile.html', form = form)

