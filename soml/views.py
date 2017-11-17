from flask import render_template, send_from_directory
from app import app


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/images/<path:path>')
def send_static(path):
    return send_from_directory('static/images/shitpics', path)