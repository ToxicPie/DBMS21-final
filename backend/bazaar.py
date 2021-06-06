import flask
import json
from .database import db_connection, fetchall_json, fetchone_json


blueprint = flask.Blueprint('bazaar_api', __name__)


@blueprint.route('/bazaar/products')
def bazaar_products():
    arg_all = flask.request.args.get('all')

    if arg_all:
        query = '''
        SELECT product_id, name
        FROM bazaar_catalogue;
        '''
    else:
        query = '''
        SELECT product_id, name
        FROM bazaar_catalogue
        WHERE enabled = 1;
        '''

    with db_connection.get_cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        return fetchall_json(cursor)


@blueprint.route('/bazaar/search')
def bazaar_search():
    return 'not yet implemented', 400


@blueprint.route('/bazaar/status')
def bazaar_status():
    return 'not yet implemented', 400
