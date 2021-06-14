import flask
import string
import datetime

from .database import DBConnection, fetchall_dict, fetchone_dict
from .hypixel_api import fetch_api


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

    with DBConnection().get_cursor() as cursor:
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

    with DBConnection().get_cursor() as cursor:
        cursor.execute(sql_stmt, (arg_query, ))
        return flask.jsonify(fetchall_dict(cursor))


@blueprint.route('/bazaar/status')
def bazaar_status():
    product_ids = flask.request.args.getlist('product_id')

    if not product_ids:
        return bad_api_request('No product IDs given')

    time_now = datetime.datetime.utcnow()

    db_connection = DBConnection()

    # query latest available data within 10min threshold
    with db_connection.get_cursor(named_tuple=True) as cursor:
        sql_stmt_latest = '''
        SELECT MAX(fetched_on) AS last_updated
        FROM bazaar_trade_history
        WHERE UNIX_TIMESTAMP(fetched_on) >= ?;
        '''
        cursor.execute(sql_stmt_latest, (time_now.timestamp() - 600.0, ))

        res = cursor.fetchone()
        if not res.last_updated:
            fetched_on = int(time_now.timestamp() * 1000)
            # fetch new data
            bazaar_data = fetch_api('skyblock/bazaar', tries=3)
            data_rows = []

            for product in bazaar_data['products'].values():
                if (product['sell_summary'] and product['buy_summary']):
                    product_id = product['product_id']
                    buy_price = product['buy_summary'][0]['pricePerUnit']
                    buy_volume = sum(order['amount']
                                     for order in product['buy_summary'])
                    sell_price = product['sell_summary'][0]['pricePerUnit']
                    sell_volume = sum(order['amount']
                                      for order in product['sell_summary'])
                    data_rows.append(
                        (product_id, time_now,
                         buy_price, buy_volume,
                         sell_price, sell_volume)
                        )

            sql_stmt = '''
            INSERT INTO bazaar_trade_history
            VALUES (?, ?, ?, ?, ?, ?);
            '''
            cursor.executemany(sql_stmt, data_rows)
            db_connection.commit()
        else:
            fetched_on = int(res.last_updated.timestamp() * 1000)

    result = {
        'updated_on': fetched_on,
        'result': []
    }

    for product_id in product_ids:
        with db_connection.get_cursor() as cursor:
            sql_stmt = '''
            SELECT
                cat.product_id,
                cat.name AS product_name,
                buy_price,
                buy_volume,
                sell_price,
                sell_volume
            FROM bazaar_catalogue cat
            RIGHT JOIN bazaar_trade_history hist
                ON cat.product_id = hist.product_id
            WHERE cat.product_id = ?
            ORDER BY fetched_on DESC
            LIMIT 1;
            '''
            cursor.execute(sql_stmt, (product_id, ))

            if not (row := fetchone_dict(cursor)):
                return bad_api_request(
                    f'{product_id} is not a valid product ID.'
                    )
            result['result'].append(row)

    return flask.jsonify(result)

import sys
@blueprint.route('/bazaar/history')
def bazaar_history():
    product_id = flask.request.args.get('product_id', '')

    sql_stmt = '''
    SELECT  UNIX_TIMESTAMP(fetched_on) AS `timestamp`,
            buy_price,
            buy_volume,
            sell_price,
            sell_volume
    FROM bazaar_trade_history
    WHERE product_id = ?;
    '''

    result = {
        'timestamps': [],
        'buy_prices': [],
        'buy_volumes': [],
        'sell_prices': [],
        'sell_volumes': []
    }

    with DBConnection().get_cursor(named_tuple=True) as cursor:
        cursor.execute(sql_stmt, (product_id, ))

        while (row := cursor.fetchone()):
            result['timestamps'].append(int(row.timestamp * 1000))
            result['buy_prices'].append(float(row.buy_price))
            result['buy_volumes'].append(row.buy_volume)
            result['sell_prices'].append(float(row.sell_price))
            result['sell_volumes'].append(row.sell_volume)

    if not result['timestamps']:
        return bad_api_request('No data found.')

    else:
        return flask.jsonify(result)
