import sqlite3
from peewee import Model, SqliteDatabase, CharField, TextField


DB = SqliteDatabase('medium.db')
DB.connect()


class Store(Model):
    url = CharField()
    title = CharField()
    text = TextField()
    tags = CharField()


    class Meta:
        database = DB


class Tags(Model):
    tags = CharField()


    class Meta:
        database = DB

DB.create_tables([Store, Tags])
DB.close()
