import pandas as pd
import matplotlib.pyplot as plt
import trade

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

    # Choose stock symbols to read
    symbols = ['AAPL','GOOGL','AMZN']
    
    # Get stock data
    df = trade.get_data(symbols, dates)
    df2 = df.ix['2009-01-22':'2010-01-28',["AAPL"]]
    #plt.plot(df2["AAPL"])
    #plt.show()
    trade.plot_data(df2)
    print df2
def multiple_stocks_on_a_graph():
    dates = pd.date_range('2016-01-01','2017-01-01')
    symbols = ['AAPL','GOOGL','AMZN']
    df = trade.get_data(symbols, dates)
    print df
    trade.plot_selected(trade.normalize_data(df),symbols,'2016-01-01','2017-01-01')
if __name__ == "__main__":
    #first_graph()
    #new_dataFrame()
    #join_dataFrame()
    #first_time_using_lib()
    multiple_stocks_on_a_graph()
    print trade.symbol_to_path("AAPL")