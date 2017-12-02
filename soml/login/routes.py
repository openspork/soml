
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from soml.login_controller import login_manager
from soml.models import User
from soml.forms import LoginForm
from soml.utils import get_redirect_target

login_mod = Blueprint('login_mod', __name__, template_folder='templates')

@login_mod.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if not form.new_user.data:
			sq = User.select().where(User.username == form.username.data)
			if sq.exists() and User.get(User.username == form.username.data).password == form.password.data:
				user = User.get(User.username == form.username.data)
				login_user(user)
				return redirect(get_redirect_target())
			else:
				flash('bad login!')
		else:
			User.create(username = form.username.data, password = form.password.data)
			user = User.get(User.username == form.username.data)
			login_user(user)
			return redirect(get_redirect_target())
	else:
		for field, errors in form.errors.items():
			for error in errors:
				flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error))

	return render_template('login.html', form = form)



@login_mod.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))