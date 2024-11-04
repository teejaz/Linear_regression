import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import seaborn as sb
import datetime as dt
import yfinance as yf

stocks = ["SPY", "GOOG"]
data = {}
for stock in stocks:
    ticker = yf.Ticker(stock)
    data[stock] = ticker.history(period="1y")["Close"]

df = pd.DataFrame(data)


returns = np.log(df).diff()
returns = returns.dropna()

correlation_matrix = returns.corr()

sample = returns.sample(60)

reg = np.polyfit(sample['SPY'], sample['GOOG'], deg = 1)
print(reg)

trend = np.polyval(reg, sample['SPY'])
plt.scatter(sample['SPY'], sample['GOOG'])
plt.plot(sample['SPY'], trend,'r')
plt.show()



print(correlation_matrix)







