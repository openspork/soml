from peewee import *
from app import db

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    uuid = UUIDField()
    title = CharField()
    creator = CharField()
    pic = CharField()
    score = IntegerField()


