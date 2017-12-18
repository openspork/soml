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

	for pic in shitpics:
		voteform = VoteForm()
		voteform.shitpic.data = pic.uuid

		#tuple of pic and corresponding form
		pics_and_forms.append( (pic, voteform) )

	if request.method == 'POST':
		#print 'POST'
		#print len(pics_and_forms)
		for pic, form in pics_and_forms:
			#print 'Validating input for', pic.name
			if form.validate_on_submit():
				#print 'validated'
				selected_pic = request.form['shitpic']
				#print selected_pic
				print pic.uuid, selected_pic
				if str(pic.uuid) == selected_pic:
					print 'pic found!'
					if form.upvote.data:
						pic.score += 1
						pic.save()
					if form.downvote.data:
						pic.score -= 1
						pic.save()

				
			

	
	return render_template('index.html', pics_and_forms = pics_and_forms)



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