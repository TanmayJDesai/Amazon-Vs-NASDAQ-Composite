import pandas as pd
import matplotlib.pyplot as plt
import calendar

file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
data_nasdaq = pd.read_csv(file_path_nasdaq)
data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
data_nasdaq['YearMonth'] = data_nasdaq['Date'].dt.to_period('M')
data_nasdaq.set_index('YearMonth', inplace=True)
data_nasdaq['Returns'] = data_nasdaq['Adj Close'].pct_change()

plt.figure(figsize=(12, 6))
plt.plot(data_nasdaq.index.astype(str), data_nasdaq['Returns'], marker='o', linestyle='-', color='blue', label='Monthly Returns')
plt.scatter(data_nasdaq.index.astype(str), data_nasdaq['Returns'], color='blue', s=50)  # Scatter points on top
plt.title('NASDAQ Composite Monthly Returns')
plt.xlabel('Year-Month')
plt.ylabel('Returns')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
