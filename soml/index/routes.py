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

	form = VoteForm()

	if request.method == 'POST':
		print 'POSTY'
		print request.form

	return render_template('index.html', current_user = current_user, shitpics = shitpics, token = token, form = form)






# to be depreciated by post request
@index_mod.route('/shitpic/<op>/<shitpic_uuid>/<token_uuid>', methods = ['GET', 'POST'])
@login_required
def shitpic_vote(op,shitpic_uuid,token_uuid):
	sq = Token.select().where(Token.uuid == token_uuid)
	if sq.exists():
		token = Token.get(Token.uuid == token_uuid)
		token.delete_instance()
		shitpic = ShitPic.get(ShitPic.uuid == shitpic_uuid)
		if op == 'up':
			shitpic.score += 1
		else:
			shitpic.score -= 1
		shitpic.save()
		return redirect(url_for('index_mod.index'))
	else:
		flash('bad token!')
	return index()