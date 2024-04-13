#!/usr/bin/env python3
"""Basic flask app with babel translation"""
from flask import g, Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Babel translation configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """Select prefered language"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the html page"""
    locale = get_locale()
    return render_template('3-index.html', current_locale=locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
