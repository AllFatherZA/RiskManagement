import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv("GasPrices2023.csv",index_col=0, parse_dates=True)
prices=df['Close']


def var_model(stock_prices, confidence_level, holding_period):
    returns = np.log(prices /prices.shift(1)).dropna() # calculate log returns
    mu = np.mean(returns) # calculate mean return
    sigma = np.std(returns) # calculate standard deviation of returns
    var =abs(mu+sigma*np.percentile(returns,100-confidence_level))*holding_period*prices[-1] # calculate Value at Risk
    return var

# Example usage
#stock_prices = pd.read_csv("stock_prices.csv", index_col=0, parse_dates=True)
confidence_level = 99 # 99% confidence level
holding_period = 1 # 1 day holding period
var = var_model(prices, confidence_level, holding_period)
print("The VaR at the {0}% confidence level for a {1}-day holding period is {2:.2f}.".format(confidence_level, holding_period, var))