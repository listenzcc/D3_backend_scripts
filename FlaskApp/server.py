# File: server.py
# Aim: Backend server in flask

import os
from flask import Flask, redirect, abort, render_template
from . import src_path
from .fix_known_issue import FixKnownIssue

# Initialization
app = Flask(__name__)
fki = FixKnownIssue()


# Response of /
@app.route('/')
def index():
    return 'Place holder of /'


# Response of file
@app.route('/<filename>')
def get_file(filename):
    path = os.path.join(src_path, filename)
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
        return fki.pipeline(filename, ''.join(lines))
    except IOError:
        return abort(404)


class Server(object):
    def __init__(self, app=app):
        self.app = app

    def run(self):
        self.app.run()
