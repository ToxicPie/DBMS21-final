import flask
from flask import Flask, render_template, url_for

blueprint = flask.Blueprint('indexpage', __name__)



@blueprint.route('/')
def index_page():
    return flask.render_template('index.html')

@blueprint.route('/products')
def products():
    return flask.render_template('products.html')

@blueprint.route('/summary/<product_id>')
def summary(product_id):
    return flask.render_template('summary.html', product_id = product_id)

@blueprint.route('/stock/<product_id>')
def stock(product_id):
    return flask.render_template('stock.html', product_id=product_id)

@blueprint.route('/stock2/<product_id>')
def stock2(product_id):
    return flask.render_template('stock2.html', product_id=product_id)

@blueprint.route('/user/')
def user():
    return flask.render_template('user.html')
