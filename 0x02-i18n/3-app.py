#!/usr/bin/env python3
"""Basic flask app with babel translation"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.jinja_env.autoescape = True
babel = Babel(app)


class Config:
    """Babel translation configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

def get_locale():
    """Select prefered language"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.route('/')
def index():
    """Render the html page"""
    ht = 'Welcome to Holberton'
    hh = 'Hello world'
    return render_template('3-index.html', home_title=ht, home_header=hh)


if __name__ == '__main__':
    app.run()
