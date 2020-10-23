# File: server.py
# Aim: Backend server in flask

import os
from flask import Flask, redirect, abort, make_response
from . import config

# Initialization
app = Flask(__name__)


# Response of /
@app.route('/')
def index():
    return 'Place holder of /'


# Response of file
@app.route('/<filename>')
def get_file(filename):
    src_path = config.query('Directory', 'src')
    path = os.path.join(src_path, filename)
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
        resp = make_response(''.join(lines), 200)
        if filename.endswith('.css'):
            resp.headers['Content-Type'] = 'text/css; charset=utf-8'
        config.logger.debug('{}'.format(resp.headers).strip())
        return resp
    except IOError:
        return abort(404)


class Server(object):
    def __init__(self, app=app):
        self.app = app

    def run(self):
        config.logger.info('Starting server')
        self.app.run()
