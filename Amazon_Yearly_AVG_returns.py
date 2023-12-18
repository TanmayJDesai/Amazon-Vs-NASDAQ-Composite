import pandas as pd
import matplotlib.pyplot as plt
import calendar

file_path = '/Users/tanmaydesai/Downloads/AMZN.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['MonthName'] = data['Month'].apply(lambda x: calendar.month_abbr[x])
data.set_index(['Year', 'MonthName'], inplace=True)
data['Returns'] = data['Adj Close'].pct_change()

plt.figure(figsize=(15, 6))
for year in data.index.get_level_values('Year').unique():
    subset = data.xs(year, level='Year')
    plt.plot(subset.index.get_level_values('MonthName'), subset['Returns'], marker='o', label=str(year))
plt.title('Amazon Monthly Returns')
plt.xlabel('Month')
plt.ylabel('Returns')
plt.xticks(rotation=45)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

