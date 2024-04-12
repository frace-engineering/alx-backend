#!/usr/bin/env python3
"""Basic flask app with babel translation"""
from flask import g, Flask, render_template, request
from flask_babel import Babel, _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel translation configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """Select prefered language"""
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


def get_user(user_id):
    """Get user information by user_id"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set user as global variable"""
    login_as = request.args.get('gotin_as')
    if login_as:
        g.user = get_user(int(login_as))
    else:
        g.user = None


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """Render the html page"""
    if g.user:
        welcome_msg = _('You are logged in\
                        as %(username)s.') % {'username': g.user['name']}
    else:
        welcome_msg = _('You are not logged in.')
    locale = get_locale()
    return render_template('5-index.html', welcome_msg=welcome_msg,
                           current_locale=locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
