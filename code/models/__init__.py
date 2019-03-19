# -*- coding: utf-8 -*-
import json
from peewee import *


class MyModel(Model):
    def to_dict(self):
        rep = {}
        for k in self._data.keys():
            if not "password" == k:
                try:
                    rep[k] = str(getattr(self, k))
                except Exception as e:
                    rep[k] = json.dumps(getattr(self, k))
        return rep


class DBUrbaner():
    def __init__(self):
        self.db = SqliteDatabase('urbaner.db')
        print ("Configuracion exitosa")

    def get_db(self):
        return self.db

    def db_connect(self):
        self.db.connect()

    def db_disconnect(self):
        self.db.close()
