from peewee import *
from soml import db

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    uuid = UUIDField()
    name = CharField()
    creator = CharField()
    date = DateTimeField() 
    score = IntegerField()

class Shits(BaseModel):
    uuid = UUIDField()
    name = CharField()
    creator = CharField()
    date = DateTimeField()
    score = IntegerField()
