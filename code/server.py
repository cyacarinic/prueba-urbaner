# -*- coding: utf-8 -*-
# Run with "python server.py"
import json
from bottle import run, get


# Index Route
@get('/', method=['OPTIONS', 'GET'])
def index():
    return json.dumps({
        "dev": "Claudio Yacarini",
        "email": "cyacarinic@gmail.com",
        "phone": "+51949194949"
    })


run(host='0.0.0.0', port=8000)
