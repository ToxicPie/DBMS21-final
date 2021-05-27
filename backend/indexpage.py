import flask


blueprint = flask.Blueprint('indexpage', __name__)


@blueprint.route('/')
def index_page():
    return flask.render_template('index.html')
