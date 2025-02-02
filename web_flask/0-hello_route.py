#!/usr/bin/python3
"""
This is a script that starts a Flask web application:
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return render_template("5-number.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
