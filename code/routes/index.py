# -*- coding: utf-8 -*-
from bottle import get
from routes import parse_response


# Index route
@get('/', method=['OPTIONS', 'GET'])
def index():
    return parse_response({
        "dev": "Claudio Yacarini",
        "email": "cyacarinic@gmail.com",
        "phone": "+51949194949"
    })
