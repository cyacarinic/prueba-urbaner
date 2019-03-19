# -*- coding: utf-8 -*-
import hashlib
import json
import jwt
from config import hash_password, jwt_secret
from bottle import abort
from bottle import get, post, request
from models.user import User
from routes import auth_verify, parse_response, enable_cors
from schemas.user import UserSchema


# Do login
@post('/login', method=['OPTIONS', 'POST'])
@enable_cors
def login():
    if request.method == 'OPTIONS':
        return {}
    else:
        body = request.json
        validated = UserSchema().load(body)

        if validated.errors:
            abort(400, validated.errors)

        password = hash_password(validated.data.get("password"))
        try:
            user = User.select().where(User.username ==
                                       validated.data.get("username")).get()
        except Exception as e:
            abort(404,
                  "User {} not found".format(validated.data.get("username")))

        if user.password == password:
            permissions = {'id': user.id, 'username': user.username}
            return parse_response({
                "login": "ok",
                "token": jwt.encode(permissions, jwt_secret,
                                    algorithm='HS256').decode("utf-8")
            })
        else:
            abort(400, "Wrong credentials.")


# Do logout
@post('/logout')
@enable_cors
def logout():
    auth_verify(dict(request.headers))
    return parse_response({"logout": "ok"})
