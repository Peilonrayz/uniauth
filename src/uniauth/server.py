from flask import Flask, request
from .unify import Unify
from .google import Google

app = Flask(__name__)
unify = Unify()
unify.add_handler(Google)


@app.route('/auth')
def auth():
    args = {
        key: value[0] if len(value) == 1 else value
        for key, value in request.args.items()
    }
    return unify.auth(**args)


@app.route('/redirect')
def redirect():
    return ''


@app.route('/token')
def token():
    return ''
