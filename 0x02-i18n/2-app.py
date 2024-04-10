#!/usr/bin/env python3
"""Basic flask app"""
from flask import g, Flask, render_template, request
from flask_babel import Babel, _
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Babel translation configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
"""Use localeselector decorator"""
def get_locale():
    """Select maching language"""
    return request.accept_language.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    """Run the app"""
    app.run()
