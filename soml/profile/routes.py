
from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from soml.login_controller import login_manager
from soml.models import User
from soml.forms import ProfileForm

profile_mod = Blueprint('profile_mod', __name__, template_folder='templates')

@profile_mod.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
	form = ProfileForm()
	return render_template('profile.html', current_user = current_user, form = form)

@profile_mod.route('/profile/delete_shitpics', methods = ['GET', 'POST'])
@login_required
def delete_shitpics():
	print request.headers
	return 'poo'