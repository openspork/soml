from flask import Flask
from peewee import PostgresqlDatabase
import psycopg2

app = Flask(__name__)

import soml.views

db = PostgresqlDatabase(
    database = 'soml',
    user = 'christian',
    password = 'flower',
    host = 'localhost'
    )

from models import *

db.connect()
print 'init db'
db.create_tables([Meme,Shit], safe = True)
db.close()

@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

