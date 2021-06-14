import mariadb
import os
import sys
import decimal


class DBConnection():

    def __init__(self, **kwargs):
        username = os.environ.get('MARIADB_USER')
        password = os.environ.get('MARIADB_PASSWORD')
        self.conn = mariadb.connect(host='mariadb',
                                    user=username,
                                    password=password,
                                    database='dbfinal',
                                    **kwargs)

    def __del__(self):
        self.conn.close()

    def get_cursor(self, **kwargs):
        return self.conn.cursor(**kwargs)

    def commit(self):
        self.conn.commit()


def _row_to_dict(row, fields):
    if row is None:
        return None
    result = dict()
    for value, field in zip(row, fields):
        if isinstance(value, decimal.Decimal):
            value = float(value)
        result[field] = value
    return result

def fetchone_dict(cursor):
    '''
    Fetches one row from a cursor and returns it as a dict.
    '''
    fields = [desc[0] for desc in cursor.description]
    return _row_to_dict(cursor.fetchone(), fields)

def fetchall_dict(cursor):
    '''
    Fetches all rows from a cursor and returns it as a list of dicts.
    '''
    fields = [desc[0] for desc in cursor.description]
    return [_row_to_dict(row, fields) for row in cursor.fetchall()]
