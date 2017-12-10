from flask import Flask
from peewee import PostgresqlDatabase
import psycopg2
from flask_uploads import UploadSet, IMAGES, configure_uploads
from config import Config

#app settings
app = Flask(__name__)
app.config.from_object(Config)

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

