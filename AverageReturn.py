import pandas as pd

#Find Average Return per month for 5 years for Amazon
def AmazonAvgReturn():
    file_path = '/Users/tanmaydesai/Downloads/AMZN.csv'
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data['Returns'] = data['Adj Close'].pct_change()
    average_return_rate = data['Returns'].mean() * 100
    print(f"Average Return Rate: {average_return_rate:.2f}%")

#Find Average Return per month for 5 years for NASDAQ
def NASDAQAvgReturn():
    import pandas as pd
    file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
    data_nasdaq = pd.read_csv(file_path_nasdaq)
    data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
    data_nasdaq['Returns'] = data_nasdaq['Adj Close'].pct_change()
    average_return_rate_nasdaq = data_nasdaq['Returns'].mean() * 100
    print(f"Average Return Rate for NASDAQ Composite: {average_return_rate_nasdaq:.2f}%")
