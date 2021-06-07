import flask
import string

from .database import db_connection, fetchall_dict, fetchone_dict


blueprint = flask.Blueprint('bazaar_api', __name__)


def bad_api_request(message):
    error = { 'error': str(message) }
    return flask.jsonify(error), 400


@blueprint.route('/bazaar/products')
def bazaar_products():
    arg_all = flask.request.args.get('all') == 'true'

    if arg_all:
        sql_stmt = '''
        SELECT product_id, name
        FROM bazaar_catalogue;
        '''
    else:
        sql_stmt = '''
        SELECT product_id, name
        FROM bazaar_catalogue
        WHERE enabled = 1;
        '''

    with db_connection.get_cursor() as cursor:
        cursor.execute(sql_stmt)
        return flask.jsonify(fetchall_dict(cursor))


@blueprint.route('/bazaar/search')
def bazaar_search():
    arg_query = flask.request.args.get('query', '').strip()
    arg_exact = flask.request.args.get('exact') == 'true'
    allowed_chars = set(string.ascii_letters + string.digits + ' ')

    if not arg_query:
        return bad_api_request(
            'param `query` is required and should be non-empty.'
            )

    # if query has unwanted characters
    if not all(char in allowed_chars for char in arg_query):
        return flask.jsonify([])

    if arg_exact:
        sql_stmt = '''
        SELECT product_id, name
        FROM bazaar_catalogue
        WHERE enabled = 1 AND
              name = ?;
        '''
    else:
        arg_query = f'%{arg_query}%'
        sql_stmt = '''
        SELECT product_id, name
        FROM bazaar_catalogue
        WHERE enabled = 1 AND
        name LIKE ?;
        '''

    with db_connection.get_cursor() as cursor:
        cursor.execute(sql_stmt, (arg_query, ))
        return flask.jsonify(fetchall_dict(cursor))


@blueprint.route('/bazaar/status')
def bazaar_status():
    return 'not yet implemented', 400
