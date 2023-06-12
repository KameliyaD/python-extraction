"""
    Download Data From Yahoo Finance using Python
"""

import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("USDT-USD", period = "1d", interval = "1m")

print(type(data))

print(data.head())

plt.plot(data.Close)

plt.show()