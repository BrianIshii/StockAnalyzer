# Forcaster 
import trade
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

now = datetime.datetime.now()
today = ("{}-{}-{}".format(now.strftime("%Y"),now.strftime("%m"),int(now.strftime("%d")) - 1))
today = "2017-01-24"
start_date = ("{}-{}-{}".format(int(now.strftime("%Y")) - 1,now.strftime("%m"),now.strftime("%d")))
start_date = "2012-08-01"
def main():
    symbols = ['SPY']
    stock = (raw_input("Which stock do you want to analyze? "))
    symbols.append(stock)
    dates = pd.date_range(start_date,today)
    df = trade.get_data(symbols,dates)
    '''five_day_future = df.shift(30)
    five_day_future.ix[0:30] = 0
    five_day_future = five_day_future.rename(columns={"AAPL":"FDF"})
    print five_day_future['FDF']
    df = df.join(five_day_future['FDF'])
    '''
    sharpe_ratio,cumulative_returns,average_daily_returns,std_daily_returns = trade.sharpe_ratio(df,stock,start_date, today)
    print sharpe_ratio
    print cumulative_returns
    print average_daily_returns
    print std_daily_returns
    rm,upper_band,lower_band = trade.get_bollinger_bands(stock,df[stock],20,False)
    rm = pd.DataFrame(rm)
    rm = rm.rename(columns={stock:"rm"})
    df = df.join(rm)
    upper_band = pd.DataFrame(upper_band)
    upper_band = upper_band.rename(columns={stock:"upper_band"})
    df = df.join(upper_band)
    lower_band = pd.DataFrame(lower_band)
    lower_band = lower_band.rename(columns={stock:"lower_band"})
    df = df.join(lower_band)
    df = df.dropna(subset=["rm"])
    low_price = pd.DataFrame(rm)
    low_price = low_price.rename(columns={"rm":"BUY"})
    low_price.ix[:] = 100
    high_price = pd.DataFrame(rm)
    high_price = high_price.rename(columns={"rm":"SELL"})
    high_price.ix[:] = 130
    #print high_price
    df = df.join(low_price)
    df = df.join(high_price)

    df['intersect'] = np.where(int(df['lowerband']) ==int(df[stock]), df[stock], 0)
    print df['intersect']
    '''
    #print df
    #print len(df)
    print df[stock]    #for i in range(len(df)):
    if df[stock] == df['lower_band']:
        print df[lower_band]
        #plt.plot([df[index]],[df[lower_band]],"ro")
    trade.plot_data(df)
'''
    '''
    new_date = "1"
    while new_date != "0":
        new_date = (raw_input("pick a start date"))
        dates = pd.date_range(new_date,today)
        scatter_plot(stock,symbols,dates)
    '''
def scatter_plot(symbol,symbols,dates):
    df= trade.get_data(symbols,dates)
    daily_returns = trade.compute_daily_returns(df)
    daily_returns.plot(kind='scatter',x='SPY',y=symbol)
    beta_symbol,alpha_symbol = np.polyfit(daily_returns['SPY'],daily_returns[symbol],1)
    plt.plot(daily_returns['SPY'], beta_symbol*daily_returns['SPY'] + alpha_symbol, '-',color='r')
    print "alpha of symbol: " , alpha_symbol
    print "beta of symbol: " , beta_symbol
    print daily_returns.corr(method='pearson')
def brian_price(symbol):
    if symbol == "AAPL":
        buy_price = 100
        sell_price = 130

    #plt.show()
if __name__ == "__main__":
    main()