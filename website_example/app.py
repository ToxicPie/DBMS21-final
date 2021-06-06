from sqlalchemy import create_engine
from flask import Flask, redirect, url_for, Markup, render_template, request
from datetime import time
from pandas import DataFrame
import math

app = Flask(__name__)

engine = create_engine("mysql://august:05281228@127.0.0.1:3306/dbfinal")
connection = engine.connect()

@app.route('/summary/<product>')
def summary(product):

    sql_cmd = f'select * from bazaar_trade_history where product_id = "{product}" order by fetched_on limit 30;'
    query = connection.execute(sql_cmd)
    history_data = DataFrame(query.fetchall())
    history_data.columns = query.keys()

    sql_cmd = f'select * from bazaar_buy_summary where product_id = "{product}" and fetched_on = "2021-06-03 10:58:54" order by summary_index limit 10;'
    query = connection.execute(sql_cmd)
    buy_data = DataFrame(query.fetchall())
    buy_data.columns = query.keys()

    sql_cmd = f'select * from bazaar_sell_summary where product_id = "{product}" and fetched_on = "2021-06-03 10:58:54" order by summary_index limit 10;'
    query = connection.execute(sql_cmd)
    sell_data = DataFrame(query.fetchall())
    sell_data.columns = query.keys()

    return render_template('summary.html', product=product, history_data=history_data, buy_data=buy_data, sell_data=sell_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        product = request.form["product_name"]
        return redirect(url_for("summary", product=product))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
