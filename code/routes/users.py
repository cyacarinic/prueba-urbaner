# -*- coding: utf-8 -*-
import json
from bottle import abort
from bottle import get, post, request
from config import hash_password
from routes import auth_verify, parse_response, enable_cors
from schemas.user import UserSchema
from models.user import User


# Get list of Users
@get('/users')
@enable_cors
def user_list():
    auth_verify(dict(request.headers))
    collection = []
    for user in User.select():
        collection.append(user.to_dict())
    return parse_response(collection)


# Get Specific User
@get('/users/<id>')
@enable_cors
def user_list(id):
    auth_verify(dict(request.headers))
    try:
        user = User.select().where(User.id == id).get()
    except Exception as e:
        abort(404, "User {} not found.".format(id))
    return parse_response(user.to_dict())


# Get Notes from user
@get('/users/<id>/notes')
@enable_cors
def user_list(id):
    user_token = auth_verify(dict(request.headers))
    try:
        user = User.select().where(User.id == id).get()
    except Exception as e:
        abort(404, "User {} not found.".format(id))
    if not user_token["username"] == user.username:
        abort(401, "You're not allowed to access to this collection. \
                    Use correct credentials.")
    notes = []
    for note in user.notes:
        note = note.to_dict()
        note.pop("owner")
        notes.append(note)
    return parse_response(notes)


# Save a new User
@post('/users')
@enable_cors
def user_save():
    body = request.json
    password = body.get("password", None)
    if password:
        body.update({"password": hash_password(password)})
    validated = UserSchema().load(body)

    if validated.errors:
        abort(400, validated.errors)

    userData = User(**validated.data)
    userData.save()

    return parse_response(validated.data)
