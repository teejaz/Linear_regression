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

data = yf.Ticker("SPY").history(period="1y")[["Close"]]
data['time'] = np.arange(1, len(data)+1)

reg = np.polyfit(data['time'], data["Close"], deg = 1 )

trend = np.polyval(reg, data['time'][-63:])
std = data['Close'][-63:].std()
plt.figure(figsize = (10,6))
plt.plot(data['time'], data['Close'], label = "S&P500")
plt.plot(data['time'][-63:], trend, 'r--')
plt.show()



predict = np.poly1d(reg)
print(predict(280))

sb.regplot(x='time', y='Close', fit_reg=True, data = data[-63:])
plt.show()
print(correlation_matrix)







