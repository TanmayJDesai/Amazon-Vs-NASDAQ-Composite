import pandas as pd
import matplotlib.pyplot as plt

file_path_amazon = '/Users/tanmaydesai/Downloads/AMZN.csv'
data_amazon = pd.read_csv(file_path_amazon)
data_amazon['Date'] = pd.to_datetime(data_amazon['Date'])
data_amazon['YearMonth'] = data_amazon['Date'].dt.to_period('M')
data_amazon.set_index('YearMonth', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(data_amazon.index.astype(str), data_amazon['Adj Close'], marker='o', linestyle='-', color='blue', label='Amazon')
plt.title('Amazon Stock Prices Over 5 Years')
plt.xlabel('Year-Month')
plt.ylabel('Stock Price')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
