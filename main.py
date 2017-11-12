from app import app, db
from models import Meme
import atexit

def init_db():
    print('connecting to db')
    db.connect()
    db.create_tables([Meme], safe = True)

def term_db():
    print('closing db')
    db.close()

if __name__ == '__main__':
    atexit.register(term_db)
    init_db()

    app.run(
            host = '0.0.0.0',
            port = 9000,
            debug = True
    )
