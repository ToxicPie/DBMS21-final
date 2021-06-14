import flask


blueprint = flask.Blueprint('pages', __name__)


@blueprint.route('/')
def index_page():
    return flask.render_template('index.html')


@blueprint.route('/search')
def search_page():
    return flask.render_template('search.html')
