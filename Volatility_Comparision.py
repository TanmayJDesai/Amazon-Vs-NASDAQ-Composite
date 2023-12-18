import pandas as pd
import matplotlib.pyplot as plt

#Find Average Volatility for Amazon 
def AmazonVolatility():
    import pandas as pd
    file_path_amazon = '/Users/tanmaydesai/Downloads/AMZN.csv'
    data_amazon = pd.read_csv(file_path_amazon)
    data_amazon['Date'] = pd.to_datetime(data_amazon['Date'])
    volatility_amazon_percent = data_amazon['Adj Close'].pct_change().std() * 100
    print(f"Volatility (Standard Deviation) for Amazon: {volatility_amazon_percent:.2f}%")
  
#Find Average Volatility for Amazon 
def NASDAQVolatility():
    file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
    data_nasdaq = pd.read_csv(file_path_nasdaq)
    data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
    volatility_nasdaq_percent = data_nasdaq['Adj Close'].pct_change().std() * 100
    print(f"Volatility (Standard Deviation) for NASDAQ Composite: {volatility_nasdaq_percent:.2f}%")

#Bar plot for each to visualize difference between the two above
def Visualize():
    #Handle Amazon Data
    file_path_amazon = '/Users/tanmaydesai/Downloads/AMZN.csv'
    data_amazon = pd.read_csv(file_path_amazon)
    data_amazon['Date'] = pd.to_datetime(data_amazon['Date'])
    average_return_amazon = data_amazon['Adj Close'].pct_change().mean() * 100
    volatility_amazon = data_amazon['Adj Close'].pct_change().std() * 100

    #Handle Nasdaq Composite Data
    file_path_nasdaq = '/Users/tanmaydesai/Downloads/^IXIC.csv'
    data_nasdaq = pd.read_csv(file_path_nasdaq)
    data_nasdaq['Date'] = pd.to_datetime(data_nasdaq['Date'])
    average_return_nasdaq = data_nasdaq['Adj Close'].pct_change().mean() * 100
    volatility_nasdaq = data_nasdaq['Adj Close'].pct_change().std() * 100

    #Bar Plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(['Amazon', 'NASDAQ'], [average_return_amazon, average_return_nasdaq], color=['blue', 'orange'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
    plt.title('Average Return Rate for Amazon and NASDAQ Composite')
    plt.ylabel('Average Return Rate (%)')
    plt.show()
    plt.figure(figsize=(12, 6))
    bars = plt.bar(['Amazon', 'NASDAQ'], [volatility_amazon, volatility_nasdaq], color=['blue', 'orange'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
    plt.title('Volatility for Amazon and NASDAQ Composite')
    plt.ylabel('Volatility (%)')
    plt.show()

AmazonVolatility()
NASDAQVolatility()
Visualize()
