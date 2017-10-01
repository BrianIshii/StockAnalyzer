#/usr/bin/env python3
"""
data.py is an object to look at stock data

Brian Ishii 2017
"""
import json

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol 
        
    def __repr__(self):
        pass

    def __str__(self):
        pass


    def get_json_data(self, symbol):
        f = open("stock.json", 'r')
        temp = json.load(f)
        f.close()
        return temp["Stocks"]["Tech"][symbol]
