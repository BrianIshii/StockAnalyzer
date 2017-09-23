'''
data.py is a library to look at stock data

Brian Ishii 2017
'''

import os
import pandas as pd
import math

class Data:
    def __init__(self, start_date, end_date, data_type="Adj Close"):
        self.symbols = ["SPY"]
        self.dates = self.get_dates(start_date, end_date)
        self.data_type = data_type
        self.df = self.get_data() 

    def __repr__(self):
        return "Data({!r}, {!r}, {!r})".format(
                self.symbols, self.dates, self.data_type)

    def __eq__(self):
        pass

    def get_data(self):
        """Returns a pd.DataFrame with desired data
        
        Keyword arguments:
        symbols: (List) list of symbols i.e. ["SPY", "AAPL"]
        dates: (DatetimeIndex) range of dates desired
        col: (String) column name of data requested (default "Adj Close")
        """
        df = pd.DataFrame(index=self.dates)

        for symbol in self.symbols:
            temp = pd.read_csv(self.path_to_symbol(symbol),
                    index_col="Date", usecols=["Date", self.data_type],
                    parse_dates=True, na_values = ["NaN"])
            temp = temp.rename(columns={self.data_type:symbol})
            df = df.join(temp)
            if symbol == "SPY":
                df = df.dropna(subset=["SPY"])
        return df

    def path_to_symbol(self, symbol, base_dir="Data"):
        """returns the CSV file path for the given symbol

        Keyword arguments:
        symbol: (String) stock name i.e. "AAPL"
        base_dir: (String) base directory for the file (default "Data")
        """
        path = os.getcwd()
        return os.path.join(path + "/{!s}.csv".format(symbol))
    
    def get_dates(self, start_date, end_date):
        """returns a pandas date range indexed for each day

        Keyword arguments:
        start_date: (String) YYYY-MM-DD
        end_date: (String) YYYY-MM-DD
        """
        return pd.date_range(start_date, end_date)

    def get_bollinger_bands(self, symbol, window=20):
        """returns a tuple with (rolling mean, upper_band, and
        lower_band)

        Keyword arguments:
        symbol: (String) stock symbol i.e. "AAPL"
        window: (int) number of days to include in the mean (default 20)
        """
        if symbol not in self.symbols:
            raise IndexError()
        values = self.df[symbol]
        rolling_mean = values.rolling(window=window).mean()
        rolling_std = values.rolling(window=window).std()
        upper_band = rolling_mean + rolling_std * 2
        lower_band = rolling_mean - rolling_std * 2
        return rolling_mean, upper_band, lower_band
        
