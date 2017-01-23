import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
    """
    plots selected data

    Arguments:
    df -- (pd.DataFrame) pandas dataframe
    columns -- (List) list of stock names i.e. "AAPL"
    start_index -- (date) starting date of data graphed year-month-day formmat i.e. '2017-01-01'
    end_index -- (date) ending date of data graphed year-month-day formmat i.e. '2017-01-01'
    """
    plot_data(df.ix[start_index:end_index,columns],title="Selected Data ({})-({})".format(start_index,end_index))

def symbol_to_path(symbol, base_dir="StockData"):
    """
    returns the CSV file path given the ticker symbol

    Arguments:
    symbol -- (String) stock name i.e. "AAPL"
    """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """
    Read stock data (adjusted close) for given symbols from CSV files.

    Arguments:
    symbols -- (List) list of symbols i.e. ["AAPL","GOOGL"]
    dates -- (pd.date_range) range of dates called
    """
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

def plot_data(df,title="Stock Prices"):
    """
    plots stock prices with labels

    Arguments:
    df -- (pd.DataFrame) dataframe with price and date
    """
    ax = df.plot(title=title,fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def normalize_data(df):
    """
    Normalize Data

    Arguments:
    df -- (pd.DataFrame) pandas dataframe
    """
    return df/ df.ix[0,:]
def get_bollinger_bands(symbol,values,window,plot):
    """
    Get Upper and lower bands

    Arguments:
    symbol -- (String) stock name i.e. "AAPL"
    values --(pd.Dataframe) i.e. df['AAPL']
    window -- (int) how many days i.e. 20
    plot -- (Bool) plot True or False
    """
    rm = pd.rolling_mean(values,window=window)
    rstd = pd.rolling_std(values,window=window)
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    if plot is True:
        ax = values.plot(title="Bollinger Bands", label=symbol)
        rm.plot(label="Rolling Mean", ax=ax)
        upper_band.plot(label="Upper-Band", ax=ax)
        lower_band.plot(label="Lower-Band", ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')
        plt.show()
