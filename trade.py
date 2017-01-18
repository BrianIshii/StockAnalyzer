import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
    plot_data(df.ix[start_index:end_index,columns],title="Selected Data ({})-({})".format(start_index,end_index))

def symbol_to_path(symbol, base_dir="StockData"):
    #return CSV file path given ticker symbol
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
"""Utility functions"""

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),index_col="Date",usecols= ["Date","Adj Close"],parse_dates=True,na_values = ['nan'])
        df_temp = df_temp.rename(columns={"Adj Close":symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df
#plot stock prices with labels
def plot_data(df,title="Stock Prices"):
    ax = df.plot(title=title,fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

#normalize data
def normalize_data(df):
    return df/ df.ix[0,:]
