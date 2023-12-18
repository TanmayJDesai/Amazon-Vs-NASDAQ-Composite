import pandas as pd

#Handle Data
file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
data_nasdaq = pd.read_csv(file_path_nasdaq)

# Convert 'Date' to datetime format
data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])

# Calculate the monthly returns for NASDAQ Composite
data_nasdaq['Returns'] = data_nasdaq['Adj Close'].pct_change()

# Calculate the average return rate for NASDAQ Composite in percentage
average_return_rate_nasdaq = data_nasdaq['Returns'].mean() * 100

print(f"Average Return Rate for NASDAQ Composite: {average_return_rate_nasdaq:.2f}%")


