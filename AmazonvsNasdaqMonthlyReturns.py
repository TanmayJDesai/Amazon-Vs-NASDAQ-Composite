import pandas as pd
import matplotlib.pyplot as plt

#Handle Amazon Data: 
file_path_amazon = '/Users/tanmaydesai/Downloads/AMZN.csv'

data_amazon = pd.read_csv(file_path_amazon)
data_amazon['Date'] = pd.to_datetime(data_amazon['Date'])
data_amazon['YearMonth'] = data_amazon['Date'].dt.to_period('M')
data_amazon.set_index('YearMonth', inplace=True)
data_amazon['Returns'] = data_amazon['Adj Close'].pct_change()

#Handle NASDAQ Composite Data
file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'

data_nasdaq = pd.read_csv(file_path_nasdaq)
data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
data_nasdaq['YearMonth'] = data_nasdaq['Date'].dt.to_period('M')
data_nasdaq.set_index('YearMonth', inplace=True)
data_nasdaq['Returns'] = data_nasdaq['Adj Close'].pct_change()

#Create Plot and graph on top of each other to get overlay graph
plt.figure(figsize=(12, 6))
plt.plot(data_amazon.index.astype(str), data_amazon['Returns'], marker='o', linestyle='-', color='blue', label='Amazon Returns')
plt.scatter(data_amazon.index.astype(str), data_amazon['Returns'], color='blue', s=50)
plt.plot(data_nasdaq.index.astype(str), data_nasdaq['Returns'], marker='o', linestyle='-', color='orange', label='NASDAQ Returns')
plt.scatter(data_nasdaq.index.astype(str), data_nasdaq['Returns'], color='orange', s=50)
plt.title('Amazon and NASDAQ Monthly Returns')
plt.xlabel('Year-Month')
plt.ylabel('Returns')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
