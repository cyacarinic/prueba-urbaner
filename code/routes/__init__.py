# -*- coding: utf-8 -*-
import json
import jwt
from config import jwt_secret
from bottle import error, response, abort, request


# Content Type
def parse_response(data):
    response.content_type = 'application/json'
    return json.dumps(data)


# Authorization
def auth_verify(headers):
    try:
        jwt_token = jwt.decode(headers.get("Authorization"),
                               jwt_secret, algorithms=['HS256'])
        return jwt_token
    except Exception as e:
        abort(401, "You're not allowed to access to this resource. Pls login")


# Errors
@error(400)
def error400(error):
    try:
        error_detail = json.loads(error.body)
    except Exception as e:
        error_detail = error.body
    error_data = {'status_code': 400, 'error_message': error_detail}
    return parse_response(error_data)


@error(401)
def error401(error):
    try:
        error_detail = json.loads(error.body)
    except Exception as e:
        error_detail = error.body
    error_data = {'status_code': 401, 'error_message': error_detail}
    return parse_response(error_data)


@error(404)
def error404(error):
    try:
        error_detail = json.loads(error.body)
    except Exception as e:
        error_detail = error.body
    error_data = {'status_code': 404, 'error_message': error_detail}
    return parse_response(error_data)
