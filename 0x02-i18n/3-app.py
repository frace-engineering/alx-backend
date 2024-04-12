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
    BABEL_DEFAULT_LOCALE = "fr"
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
    home_title = 'Welcome to Holberton'
    home_header = 'Hello world'
    return render_template('3-index.html', home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
