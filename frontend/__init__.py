import flask

from . import pages
from . import charts


flask_app = flask.Flask(__name__)

flask_app.config.from_pyfile('flask_config.py')

flask_app.register_blueprint(pages.blueprint)
flask_app.register_blueprint(charts.blueprint)
