import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Analysis.trade as trade

global dates

def main():
    global dates
    start_date = "2015-01-02"
    symbols = ['SPY']

    dates = pd.date_range("2015-01-02", "2015-02-02")
    symbols.append("AAPL") 
    df = trade.get_data(symbols,dates)
    print(str(df)) 
    print(df)
    graph_close(df, "AAPL")   

# 
def graph_close(df,symbol):
    #past_year = df[symbol][252:]
    past_year = df[symbol][5:]
    past_year
    print(type(past_year[0]))
    #need to change it to float
    #df[symbol].hist(bins=2,label = symbol)
    #past_year.hist(bins=2,label = "Past Year")
    #plt.legend(loc="upper right")
    #past_year_mean = past_year.mean()
    #past_year_std = past_year.std()
    #mean = df[symbol].mean()
    #print("mean = " + str(mean))
    #std = df[symbol].std()
    #print("std = " + str(std))
    #simplify with func
    #plt.axvline(mean,color='w',linestyle="dashed",linewidth=2)
    #plt.axvline(std + mean,color='r',linestyle="dashed",linewidth=2)
    #plt.axvline(-std + mean,color='r',linestyle="dashed",linewidth=2)
    #plt.axvline(past_year_mean,color='w',linewidth=2)
    #plt.axvline(past_year_std + past_year_mean,color='r',linewidth=2)
    #plt.axvline(-past_year_std + past_year_mean,color='r',linewidth=2)
    #plt.axvline(df[symbol][-1],color='black',linewidth=2)
    #print(df.kurtosis())

def buy_sell(df,symbol):
    rm,upper_band,lower_band = trade.get_bollinger_bands(symbol,df[symbol],20,False)
    rm = pd.DataFrame(rm)
    rm = rm.rename(columns={symbol:"rm"})
    df = df.join(rm)
    upper_band = pd.DataFrame(upper_band)
    upper_band = upper_band.rename(columns={symbol:"upper_band"})
    df = df.join(upper_band)
    lower_band = pd.DataFrame(lower_band)
    lower_band = lower_band.rename(columns={symbol:"lower_band"})
    df = df.join(lower_band)
    df = df.dropna(subset=["rm"])
    add = float(df[symbol][0]/1000)
    df['sell_points'] = (df[symbol] >= df["upper_band"]-add).astype(float)
    df['buy_points'] = (df[symbol] <= df["lower_band"]+add).astype(float)
    df['sell'] = 0
    df['buy'] = 0
    df['sell'][df['sell_points'] == 1] = df[symbol]
    df['sell'][df['sell_points'] == 0] = "NaN"
    df['buy'][df['buy_points'] == 1] = df[symbol]
    df['buy'][df['buy_points'] == 0] = "NaN"
    plt.plot(df['sell'],'go')
    plt.plot(df["buy"],'ro')
    plt.plot(df[symbol])
    plt.plot(df['lower_band'],'r')
    plt.plot(df['upper_band'],'g')

def volume(df,symbol):
    global dates
    symbols = [symbol]
    df_vol = trade.get_data(symbols,dates,"Volume")
    df_vol = df_vol.rename(columns={symbol:"Volume"})
    df_vol = (df_vol/1000000)
    plt.plot(df[symbol])
    plt.plot(df_vol["Volume"])
    print(df_vol)

def scatter_plot(symbol,symbols):
    global dates
    df= trade.get_data(symbols,dates)
    daily_returns = trade.compute_daily_returns(df)
    daily_returns.plot(kind='scatter',x='SPY',y=symbol)
    beta_symbol,alpha_symbol = np.polyfit(daily_returns['SPY'],daily_returns[symbol],1)
    plt.plot(daily_returns['SPY'], beta_symbol*daily_returns['SPY'] + alpha_symbol, '-',color='r')
    print("alpha of symbol: " , alpha_symbol)
    print("beta of symbol: " , beta_symbol)
    print(daily_returns.corr(method='pearson'))

if __name__ == "__main__":
    main()
