import pandas as pd
import matplotlib.pyplot as plt
import calendar

#Handle Data
file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
data_nasdaq = pd.read_csv(file_path_nasdaq)

# Convert 'Date' to datetime format
data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])

# Extract the month and year from the 'Date' column
data_nasdaq['Month'] = data_nasdaq['Date'].dt.month
data_nasdaq['Year'] = data_nasdaq['Date'].dt.year

# Create a new column for month names
data_nasdaq['MonthName'] = data_nasdaq['Month'].apply(lambda x: calendar.month_abbr[x])

# Set the 'Year' and 'MonthName' columns as the index
data_nasdaq.set_index(['Year', 'MonthName'], inplace=True)

# Calculate the monthly returns
data_nasdaq['Returns'] = data_nasdaq['Adj Close'].pct_change()
plt.figure(figsize=(15, 6))
unique_years = data_nasdaq.index.get_level_values('Year').unique()
for i, year in enumerate(unique_years):
    subset = data_nasdaq.xs(year, level='Year')
    color = plt.cm.get_cmap('tab10')(i / len(unique_years))  # Use tab10 colormap for distinct colors
    plt.plot(subset.index.get_level_values('MonthName'), subset['Returns'], marker='o', linestyle='-', label=str(year), color=color)
plt.title('NASDAQ Composite Monthly Returns')
plt.xlabel('Month')
plt.ylabel('Returns')
plt.xticks(rotation=45)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
