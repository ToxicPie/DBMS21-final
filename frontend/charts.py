import flask


blueprint = flask.Blueprint('charts', __name__)


@blueprint.route('/stock/<string:product_id>')
def stock(product_id):
    return flask.render_template('stock.html', product_id=product_id)

@blueprint.route('/stock2/<string:product_id>')
def stock2(product_id):
    return flask.render_template('stock2.html', product_id=product_id)

@blueprint.route('/history/<string:product_id>')
def history(product_id):
    return flask.render_template('chart.html', product_id=product_id)
