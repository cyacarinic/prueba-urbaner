# Run with "python client.py"
from bottle import get, run, static_file

@get('/')
def index():
    return static_file('index.html', root=".")

@get('/docs')
def docs():
    return static_file('docs.html', root=".")

run(host='localhost', port=5000)
