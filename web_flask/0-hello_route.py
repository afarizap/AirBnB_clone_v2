#!/usr/bin/python3
""" import flask to print hello world from localhost """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """ return a string with hello world """
    return 'Hello, World!'


app.run()
