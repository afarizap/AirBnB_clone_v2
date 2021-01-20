#!/usr/bin/python3
""" import flask to print hello world from localhost """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ return a string w, ith hello world """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
