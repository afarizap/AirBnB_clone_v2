#!/usr/bin/python3
""" import flask to print hello world from localhost """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return a string with Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return a string with HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def route_c(text):
    """ return a string with C + string """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def route_python(text='is cool'):
    """ display “Python ”, followed by the value of the text variable  """
    if text:
        return 'Python {}'.format(text.replace('_', ' '))
    else:
        return 'Python is cool'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
