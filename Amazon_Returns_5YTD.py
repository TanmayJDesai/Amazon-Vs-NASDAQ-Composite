import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/tanmaydesai/Downloads/AMZN.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data['YearMonth'] = data['Date'].dt.to_period('M')
data.set_index('YearMonth', inplace=True)
data['Returns'] = data['Adj Close'].pct_change()

plt.figure(figsize=(12, 6))
plt.plot(data.index.astype(str), data['Returns'], marker='o', linestyle='-', color='blue', label='Monthly Returns')
plt.scatter(data.index.astype(str), data['Returns'], color='blue', s=50)  # Scatter points on top
plt.title('Amazon Monthly Returns')
plt.xlabel('Year-Month')
plt.ylabel('Returns')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
