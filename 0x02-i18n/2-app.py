#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Babel translation configurations"""
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

"""@babel.localeselector"""
def get_locale():
    """Select maching langusge"""
    return request.accept_language.best_match(app.config['LANGUSGE'])



@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Render the html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
