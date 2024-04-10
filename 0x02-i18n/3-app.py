#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


#@babel.localeselector
def get_locale():
    return request.accept_language.best_match(app.config['LANGUSGE'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
