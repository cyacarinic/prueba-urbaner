# -*- coding: utf-8 -*-
# import logging
from bottle import run
from models.note import Note
from models.user import User

# Import routes module
from routes import index, notes, users, login

# Create tables if not exists
Note.create_table(True)
User.create_table(True)

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Program starts running now")

# Run server
run(host='0.0.0.0', port=8000)
