from flask import Blueprint, flash, redirect, request, render_template, url_for
from flask_login import login_user, logout_user, login_required, current_user
from uuid import uuid4
from soml.models import *
from soml.forms import VoteForm


index_mod = Blueprint('index_mod', __name__, template_folder='templates')

@index_mod.route('/', methods = ['GET', 'POST'])
def index():
	shitpics = ShitPic.select().order_by(ShitPic.score.desc())
	token = Token.create(uuid = uuid4())

	pics_and_forms = []

	for pic in shitpics:
		form = VoteForm()
		#tuple of pic and corresponding form
		pics_and_forms.append( (pic, form) )

	if form.validate_on_submit():
		for pic_and_form in pics_and_forms:
			if pic_and_form[1].upvote.data:
				pic_and_form[0].score += 1
				pic_and_form[0].save()
			if pic_and_form[1].downvote.data:
				pic_and_form[0].score += 1
				pic_and_form[0].save()

	return render_template('index.html', current_user = current_user, shitpics = shitpics, token = token, pics_and_forms = pics_and_forms)



# to be depreciated by post request
# @index_mod.route('/shitpic/<op>/<shitpic_uuid>/<token_uuid>', methods = ['GET', 'POST'])
# @login_required
# def shitpic_vote(op,shitpic_uuid,token_uuid):
# 	sq = Token.select().where(Token.uuid == token_uuid)
# 	if sq.exists():
# 		token = Token.get(Token.uuid == token_uuid)
# 		token.delete_instance()
# 		shitpic = ShitPic.get(ShitPic.uuid == shitpic_uuid)
# 		if op == 'up':
# 			shitpic.score += 1
# 		else:
# 			shitpic.score -= 1
# 		shitpic.save()
# 		return redirect(url_for('index_mod.index'))
# 	else:
# 		flash('bad token!')
# 	return index()