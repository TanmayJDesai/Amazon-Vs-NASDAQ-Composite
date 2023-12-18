import pandas as pd
import matplotlib.pyplot as plt

file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
data_nasdaq = pd.read_csv(file_path_nasdaq)
data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
data_nasdaq['YearMonth'] = data_nasdaq['Date'].dt.to_period('M')
data_nasdaq.set_index('YearMonth', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(data_nasdaq.index.astype(str), data_nasdaq['Adj Close'], marker='o', linestyle='-', color='orange', label='NASDAQ Composite')

plt.title('NASDAQ Composite Stock Prices Over 5 Years')
plt.xlabel('Year-Month')
plt.ylabel('Stock Price')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
