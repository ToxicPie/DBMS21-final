import flask

from . import indexpage


flask_app = flask.Flask(__name__)

flask_app.config.from_pyfile('flask_config.py')

flask_app.register_blueprint(indexpage.blueprint)
