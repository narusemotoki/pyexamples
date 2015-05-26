#!/usr/bin/env python3
from bottle import route, run, default_app


@route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=8000)
else:
    application = default_app()
