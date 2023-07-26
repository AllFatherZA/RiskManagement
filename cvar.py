import pandas as pd
import numpy as np

# Read gas prices from CSV file
df = pd.read_csv('GasPrices2023.csv')
gas_prices = df['Close'].values

# Calculate CVaR
confidence_level = 0.95  # Set the desired confidence level
sorted_prices = np.sort(gas_prices)
num_samples = len(sorted_prices)
cvar_index = int((1 - confidence_level) * num_samples)
cvar = np.mean(sorted_prices[:cvar_index])

# Print CVaR result
print(f"CVaR at {confidence_level*100}% confidence level: {cvar}")
