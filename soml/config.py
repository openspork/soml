import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOADED_SHITPICS_DEST = 'data/images/shitpics/'
    UPLOADED_SHITPICS_URL = 'images/'
    