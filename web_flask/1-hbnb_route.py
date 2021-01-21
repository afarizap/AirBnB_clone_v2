#!/usr/bin/python3
""" import flask to print hello world from localhost """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return a string w, ith hello world """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return a string w, ith hello world """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
