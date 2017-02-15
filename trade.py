'''
Trade.py is a library to look at stock data
Written by Brian Ishii 2017

'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import math
import updateData

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

def path_to_symbol(symbol, base_dir="StockData"):
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
        df_temp = pd.read_csv(path_to_symbol(symbol),index_col="Date",usecols= ["Date","Adj Close"],parse_dates=True,na_values = ['nan'])
        df_temp = df_temp.rename(columns={"Adj Close":symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df

def plot_data(df,title="Stock Prices",ylabel="Prices"):
    """
    plots stock prices with labels

    Arguments:
    df -- (pd.DataFrame) dataframe with price and date
    """
    ax = df.plot(title=title,fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
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
    return rm,upper_band,lower_band
def compute_daily_returns(df):
    """
    Compute the Daily returns of a stock

    Arguments:
    df -- (pd.DataFrame) i.e. df['AAPL']
    """
    daily_returns = ((df / df.shift(1))-1)
    daily_returns.ix[0,:] = 0
    return daily_returns
def daily_returns_hist(symbols,dates):
    """
    Read stock data (adjusted close) for given symbols from CSV files.

    Arguments:
    symbols -- (List) list of symbols i.e. ["AAPL","GOOGL"]
    dates -- (pd.date_range) range of dates called
    """
    df = get_data(symbols,dates)
    daily_returns = compute_daily_returns(df)
    for symbol in symbols:
        daily_returns[symbol].hist(bins=20,label = symbol)
    plt.legend(loc="upper right")
    if len(symbols) == 1:
        mean = daily_returns['SPY'].mean()
        print "mean = " + str(mean)
        std = daily_returns['SPY'].std()
        plt.axvline(mean,color='w',linestyle="dashed",linewidth=2)
        plt.axvline(std,color='r',linestyle="dashed",linewidth=2)
        plt.axvline(-std,color='r',linestyle="dashed",linewidth=2)
        print daily_returns.kurtosis()
    plt.show()
def compute_cumulative_returns(df, start_index, end_index):
    """
    compute the cumulative returns of a stock in a time period

    Arguments:
    df -- (pd.DataFrame) i.e. df['AAPL']
    start_index -- (date) starting date of data graphed year-month-day formmat i.e. '2017-01-01'
    end_index -- (date) ending date of data graphed year-month-day formmat i.e. '2017-01-01'
    """
    cumulative_returns = (df.loc[end_index]/df.loc[start_index])-1
    return cumulative_returns
def sharpe_ratio(df,symbol,start_index, end_index):
    """
    computes the sharpe ratio returns sharpe, c, mean, and std

    Arguments:
    df -- (pd.DataFrame) i.e. df['AAPL']
    start_index -- (date) starting date of data graphed year-month-day formmat i.e. '2017-01-01'
    end_index -- (date) ending date of data graphed year-month-day formmat i.e. '2017-01-01'
    """
    d = compute_daily_returns(df)
    c = compute_cumulative_returns(df,start_index,end_index)
    mean = d[symbol].mean()
    std = d[symbol].std()
    sharpe = math.sqrt(252)*(mean/std)
    return sharpe,c,mean,std

def check_data(today):
    """
    Checks Date and updates the CSV data files if necessary

    Arguments:
    today -- (String) string in date form i.e. '2017-01-01'
    """
    df_check = pd.read_csv(path_to_symbol("SPY"))
    date = df_check["Date"][0]
    if date != today:
        if int(now.strftime('%w')) == 1:
            print("Data up to date")
            return
        else:
            updateData.update_data("StockData")
            return
    else: 
        print("Data up to date")
        return
