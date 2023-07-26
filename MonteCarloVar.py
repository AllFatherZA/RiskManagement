import numpy as np
import pandas as pd

# Load gas prices from CSV file using pandas
gas_prices_df = pd.read_csv('GasPrices2023.csv')

# Extract gas prices close  column from DataFrame
gas_prices = gas_prices_df['Close']

# Calculate the daily returns
returns = gas_prices.pct_change().dropna()

# Calculate the volatility and mean return
volatility = returns.std()
mean_return = returns.mean()

# Define the parameters for gas prices simulation
initial_price = gas_prices.iloc[-1]  # Use the last price as the initial price
num_simulations = 10000  # Number of simulations
confidence_level = 0.95  # Confidence level for VaR estimation

# Simulate gas price paths using geometric Brownian motion
np.random.seed(42)  # Set a random seed for reproducibility
price_paths = np.zeros((num_simulations, 365))  # 365 days in 2023

for i in range(num_simulations):
    price_paths[i, 0] = initial_price

    for day in range(1, 365):
        drift = mean_return * (1 / 365)
        shock = volatility * np.random.randn() * np.sqrt(1 / 365)
        price_paths[i, day] = price_paths[i, day - 1] * (1 + drift + shock)

# Calculate daily returns for each simulation
returns = (price_paths[:, 1:] - price_paths[:, :-1]) / price_paths[:, :-1]

# Calculate the portfolio value at the end of 2023
portfolio_value = 1000000  # Example portfolio value
portfolio_returns = portfolio_value * returns

# Calculate the VaR
sorted_portfolio_returns = np.sort(portfolio_returns)
var_index = int(num_simulations * (1 - confidence_level))
var = -sorted_portfolio_returns[var_index]

# Print the VaR estimation
print(f"VaR ({confidence_level * 100}% confidence level) for 2023 gas prices: {var:.2f}")
