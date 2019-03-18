# -*- coding: utf-8 -*-
import json
from bottle import response


# Content Type
def parse_response(data):
    response.content_type = 'application/json'
    return json.dumps(data)
