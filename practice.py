import pandas as pd
import matplotlib.pyplot as plt
import trade
import numpy as np
def first_graph():
    df = pd.read_csv("StockData/AAPL_stock_history.csv")
    plt.plot(df["Adj Close"])
    print df
    plt.show()

def new_dataFrame():
	#define date range
    start_date = "2016-01-22"
    end_date = "2016-12-26"
    dates = pd.date_range(start_date,end_date)

    #create empty data frame
    df1 = pd.DataFrame(index = dates)

    #Read AAPL data
    df_AAPL = pd.read_csv("StockData/AAPL_stock_history.csv",index_col = "Date",parse_dates=True,na_values = ['nan'])
    new_df = df1.join(df_AAPL)
    new_df = new_df.dropna()
    plt.plot(new_df["Adj Close"])
    plt.show()
    print new_df

def join_dataFrame():
	#set range for df1
    start_date = "1999-01-22"
    end_date = "2016-12-26"
    dates = pd.date_range(start_date,end_date)

    #create empty data frame
    df1 = pd.DataFrame(index = dates)

    #Read AAPL data
    df_AAPL = pd.read_csv("StockData/AAPL_stock_history.csv",index_col = "Date",usecols=["Date","Adj Close"],parse_dates=True,na_values = ['nan'])

    #Rename 'Adj Close' to  "AAPL"
    df_AAPL = df_AAPL.rename(columns={'Adj Close':'AAPL'})

    df1 = df1.join(df_AAPL, how = 'inner')
    df1 = df1.dropna()

    #read SPY data
    df_SPY = pd.read_csv("StockData/SPY_stock_history.csv",index_col = "Date",usecols=["Date","Adj Close"],parse_dates=True,na_values = ['nan'])
    df_SPY = df_SPY.rename(columns={'Adj Close':'SPY'})

    #join df_SPY with df1
    df1 = df1.join(df_SPY)

    print df1
    plt.plot(df1[["AAPL","SPY"]])
    plt.show()

def first_time_using_lib():
    # Define a date range
    dates = pd.date_range('2009-01-22', '2010-01-26')
    print dates
    # Choose stock symbols to read
    symbols = ['AAPL','GOOGL','AMZN']

    # Get stock data
    df = trade.get_data(symbols, dates)
    df2 = df.ix['2009-01-22':'2010-01-28',["AAPL"]]
    #plt.plot(df2["AAPL"])
    #plt.show()
    trade.plot_data(df2)
    print df2
    print df2.std()
def multiple_stocks_on_a_graph():
    dates = pd.date_range('2016-01-01','2017-01-01')
    symbols = ['AAPL','GOOGL','AMZN']
    df = trade.get_data(symbols, dates)
    print df
    trade.plot_selected(trade.normalize_data(df),symbols,'2016-01-01','2017-01-01')
def rolling_mean_prac():
    dates = pd.date_range('2016-01-01','2016-12-31')
    symbols = ['AAPL']
    df = trade.get_data(symbols, dates)
    print trade.compute_cumulative_returns(df,'2016-01-11','2016-12-30')
    trade.get_bollinger_bands("AAPL",df['AAPL'],20,True)
    daily_returns = trade.compute_daily_returns(df)
    trade.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

"""
    ax = df['SPY'].plot(title="SPY rolling mean",label='SPY')
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    rm_SPY.plot(label="Rolling mean", ax=ax)
    rstd_SPY = pd.rolling_std(df['SPY'],window=20)
    upper_band = rm_SPY + rstd_SPY*2
    lower_band = rm_SPY - rstd_SPY*2
    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)
    ax.set_xlabel("Price")
    ax.set_ylabel("Date")
    ax.legend(loc="upper left")
    plt.show()
"""
def hist_prac():
    dates = pd.date_range('2016-01-01','2016-12-31')
    symbols = ['SPY','AAPL']
    #trade.daily_returns_hist(symbols, dates)
    df= trade.get_data(symbols,dates)
    daily_returns = trade.compute_daily_returns(df)
    daily_returns['AAPL'].hist(bins=20,label = "AAPL")

    daily_returns['SPY'].hist(bins=20,label="SPY")
    plt.legend(loc="upper right")

    '''
    mean = daily_returns['SPY'].mean()
    print "mean = " + str(mean)
    std = daily_returns['SPY'].std()

    plt.axvline(mean,color='w',linestyle="dashed",linewidth=2)
    plt.axvline(std,color='r',linestyle="dashed",linewidth=2)
    plt.axvline(-std,color='r',linestyle="dashed",linewidth=2)
    print daily_returns.kurtosis()
    '''
    plt.show()
def scat_prac():
    dates = pd.date_range('2016-01-01','2016-12-31')
    symbols = ['SPY','AAPL']
    df= trade.get_data(symbols,dates)
    daily_returns = trade.compute_daily_returns(df)
    daily_returns.plot(kind='scatter',x='SPY',y="AAPL")
    beta_AAPL,alpha_AAPL = np.polyfit(daily_returns['SPY'],daily_returns['AAPL'],1)
    plt.plot(daily_returns['SPY'], beta_AAPL*daily_returns['SPY'] + alpha_AAPL, '-',color='r')
    print "alpha of AAPL: " , alpha_AAPL
    print "beta of AAPL: " , beta_AAPL
    print daily_returns.corr(method='pearson')
    print trade.sharpe_ratio(df,"AAPL",'2016-01-12','2016-12-20')

    plt.show()
if __name__ == "__main__":
    #first_graph()
    #new_dataFrame()
    #join_dataFrame()
    #first_time_using_lib()
    #multiple_stocks_on_a_graph()
    #rolling_mean_prac()
    #print trade.symbol_to_path("AAPL")
    #hist_prac()
    #scat_prac()
