from peewee import *
from flask_login import UserMixin

from app import db

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    uuid = UUIDField()
    name = CharField()
    creator = CharField()
    date = DateTimeField() 
    score = IntegerField(default = 0)

class User(UserMixin, BaseModel):
    username = CharField(unique=True)
    password = CharField()

class ShitPic(BaseModel):
    user = ForeignKeyField(User, related_name='shitpics')
    uuid = UUIDField()
    filename = CharField()
    name = CharField()
    date = DateTimeField()
    score = IntegerField(default = 0)
