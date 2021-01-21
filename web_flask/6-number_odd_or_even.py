#!/usr/bin/python3
""" import flask to print hello world from localhost """
from flask import Flask, render_template

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
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def route_number(n):
    """ display number and the number provided if is an integer"""
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def route_n_template(n):
    """ display number and the number provided if is an integer"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def route_odd_even(n):
    """ display number and the number provided if is an integer"""
    page = "6-number_odd_or_even.html"
    if n % 2:
        return render_template(page, number=n, odd_even="odd")
    else:
        return render_template(page, number=n, odd_even="even")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
