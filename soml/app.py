from flask import Flask
from peewee import PostgresqlDatabase
import psycopg2
from flask_uploads import UploadSet, IMAGES, configure_uploads

#app settings
app = Flask(__name__)
app.config.update(
	SECRET_KEY = 'secret',
	UPLOADED_SHITPICS_DEST = 'soml/static/images/shitpics/',
	UPLOADED_SHITPICS_URL = 'images/'
	)


#db settings
db = PostgresqlDatabase(
    database = 'soml',
    user = 'christian',
    password = 'flower',
    host = 'localhost'
    )

#upload settings
shitpics = UploadSet('shitpics', IMAGES)
configure_uploads(app, shitpics)
