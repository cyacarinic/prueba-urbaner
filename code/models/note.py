# -*- coding: utf-8 -*-
from peewee import *
from models import DBUrbaner, MyModel
from models.user import User


class Note(MyModel):
    title = CharField()
    content = CharField()
    owner = ForeignKeyField(User, related_name='notes')

    class Meta:
        database = DBUrbaner().get_db()
