from flask import Flask

from app import app
from views import *
from models import *

db.connect()
print 'init db'
db.create_tables([Meme,ShitPic,User], safe = True)
db.close()

@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

#blueprints
from upload_shit.routes import mod
app.register_blueprint(mod)

from login.routes import login_mod
app.register_blueprint(login_mod)