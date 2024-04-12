#!/usr/bin/env python3
"""Basic flask app with babel translation support"""
from flask import g, Flask, render_template, request
from flask_babel import Babel, _
app = Flask(__name__)


class Config:
    """Configuration settings for babel translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """
    Select the appropriate language for translation

    Return:
        locale.
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


"""Instantaite babel with locale_selector()"""
babel = Babel(app, locale_selector=get_locale)
app.config.from_object(Config)


@app.route('/')
def index():
    """Render the html page"""
    ht = 'Welcome to Holberton'
    hh = 'Hwllo world'
    locale = get_locale()
    return render_template('2-index.html', home_title=ht, home_header=hh,
                           current_locale=locale)


if __name__ == '__main__':
    """Run the app as main"""
    app.run(host='0.0.0.0', port=5000, debug=True)
