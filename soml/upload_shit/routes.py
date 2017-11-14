from flask import Blueprint, render_template, send_from_directory
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

mod = Blueprint('upload_shit', __name__, template_folder='templates')

@mod.route('/upload_shit', methods = ['GET', 'POST'])
def upload_shit():
	return render_template('upload_shit.html')


	