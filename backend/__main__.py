import flask

from . import indexpage


flask_app = flask.Flask(__name__)

flask_app.config.from_pyfile('flask_config.py')

flask_app.register_blueprint(indexpage.blueprint)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8000)
