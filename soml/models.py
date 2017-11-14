from peewee import *
from app import db

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    uuid = UUIDField()
    name = CharField()
    creator = CharField()
    date = DateTimeField() 
    score = IntegerField()

class Shit(BaseModel):
    uuid = UUIDField()
    name = CharField()
    creator = CharField()
    date = DateTimeField()
    score = IntegerField()
