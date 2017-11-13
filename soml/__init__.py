from flask import Flask
from peewee import PostgresqlDatabase
import psycopg2

app = Flask(__name__)

db = PostgresqlDatabase(
    database = 'soml',
    user = 'christian',
    password = 'flower',
    host = 'localhost'
    )


import soml.views
