from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from uuid import uuid4
from soml.models import *
from soml.forms import VoteForm


index_mod = Blueprint('index_mod', __name__, template_folder='templates')

@index_mod.route('/', methods = ['GET', 'POST'])
def index(shitpic_uuid = None):
	shitpics = ShitPic.select().order_by(ShitPic.score.desc())


	pics_and_forms = []
	pics_and_forms_dict = {}

	for pic in shitpics:
		voteform = VoteForm()
		voteform.shitpic.data = pic.uuid
		pics_and_forms.append( (pic, voteform) )
		pics_and_forms_dict[pic.uuid] = voteform

	if request.method == 'POST':
		for pic, form in pics_and_forms:
			if form.validate_on_submit():
				selected_pic = request.form['shitpic']
				print pic.uuid, selected_pic
				if str(pic.uuid) == selected_pic:
					if form.upvote.data:
						pic.score += 1
						pic.save()
					if form.downvote.data:
						pic.score -= 1
						pic.save()

	return render_template('index.html', pics_and_forms = pics_and_forms)
