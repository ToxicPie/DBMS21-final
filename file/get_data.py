# -*- coding: utf-8 -*-
"""database.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x6HXDHGxlyZ-B5VkfULEpDfvhcwzXxmH
"""

import requests
import json
url = 'https://api.hypixel.net/skyblock/bazaar'
data = requests.get(url).json()

import pandas as pd
import time
import datetime as dt
products = [k for k in data['products']]
df = pd.read_json(json.dumps(data['products']), typ='series')

# bazaar_catalogue = pd.DataFrame()
# bazaar_catalogue['name'] = df.keys()
# bazaar_catalogue['product_id'] = [p['product_id'] for p in df]

bazaar_trade_history = pd.DataFrame()
bazaar_trade_history['product_id'] = [p['quick_status']['productId'] for p in df]
bazaar_trade_history['fetched_on'] = [dt.datetime.utcfromtimestamp(data['lastUpdated']/1000).strftime("%Y/%m/%d %H:%M:%S.%f")] * len(df)
bazaar_trade_history['buy_price'] = [p['quick_status']['buyPrice'] for p in df]
bazaar_trade_history['buy_volume'] = [p['quick_status']['buyVolume'] for p in df]
bazaar_trade_history['sell_price'] = [p['quick_status']['sellPrice'] for p in df]
bazaar_trade_history['sell_volume'] = [p['quick_status']['sellVolume'] for p in df]

# bazaar_catalogue.to_csv('/home/august/github/DBMS21-final/file/bazaar_catalogue.csv', index=False)
bazaar_trade_history.to_csv('/home/august/github/DBMS21-final/file/bazaar_trade_history.csv', mode='a', index=False, header=False)
