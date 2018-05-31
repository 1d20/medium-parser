import sqlite3
from peewee import Model, SqliteDatabase, CharField, TextField


DB = SqliteDatabase('medium.db')
DB.connect()


class Store(Model):
    url = CharField(default="")
    title = CharField(default="")
    text = TextField(default="")
    tags = CharField(default="")


    class Meta:
        database = DB

DB.create_tables([Store])
DB.close()
