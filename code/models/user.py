# -*- coding: utf-8 -*-
from peewee import *
from models import DBUrbaner, MyModel


class User(MyModel):
    username = CharField()
    password = CharField()

    class Meta:
        database = DBUrbaner().get_db()
