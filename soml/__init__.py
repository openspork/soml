from flask import Flask
from app import app
from views import *

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


#blueprints demo
from upload_shit.routes import mod
app.register_blueprint(mod)
 