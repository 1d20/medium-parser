import sqlite3
from peewee import Model, SqliteDatabase, CharField, TextField, ForeignKeyField, IntegerField


DB = SqliteDatabase('medium.db')
DB.connect()


class Tags(Model):
    tags_id = IntegerField()
    tags = CharField()


    class Meta:
        database = DB


class Store(Model):
    url = CharField()
    title = CharField()
    text = TextField()
    tags = ForeignKeyField(Tags)


    class Meta:
        database = DB


DB.create_tables([Tags, Store])
DB.close()
