#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel, _
app = Flask(__name__)


class Config:
    """Configurations for the babel translatiion"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Render the html page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
