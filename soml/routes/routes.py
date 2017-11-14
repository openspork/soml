from flask import Blueprint
from soml.app import db

mod = Blueprint('upload_shit', __name__)

@mod.route('/upload_shit')
def upload_shit():
	return 'upload_shit'