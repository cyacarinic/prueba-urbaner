# -*- coding: utf-8 -*-
from bottle import get
from routes import parse_response, enable_cors


# Index route
@get('/', method=['OPTIONS', 'GET'])
@enable_cors
def index():
    return parse_response({
        "dev": "Claudio Yacarini",
        "email": "cyacarinic@gmail.com",
        "phone": "+51949194949"
    })
