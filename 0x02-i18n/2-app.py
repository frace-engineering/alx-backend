#!/usr/bin/env python3
"""Basic flask app with babel translation"""
from flask import g, Flask, render_template, request
from flask_babel import Babel, _
app = Flask(__name__)


class Config:
    """Babel translation configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""Configure the babel app"""
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """Select maching language"""
    """Get user attribute from the flask.g module"""
    user = getattr(g, 'user', None)
    if user is not None:
        """return the user's set locale"""
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    """Run the app as main"""
    app.run(host='0.0.0.0', port=5001, debug=True)
