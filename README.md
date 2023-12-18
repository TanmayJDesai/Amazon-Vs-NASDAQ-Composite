# Amazon vs NASDAQ Composite Stock, Average Return and Average Volatility Comparision

# Stock Analysis: Amazon vs NASDAQ

This project analyzes and compares the stock performance of Amazon and the NASDAQ Composite index over the past 5 years. It includes visualizations of average returns and volatility.

## Data Collection

To replicate the analysis with the same dataset, follow these steps to obtain the historical stock data for Amazon and the NASDAQ Composite from Yahoo Finance:

1. **Amazon Data:**
   - Visit the [Amazon page on Yahoo Finance](https://finance.yahoo.com/quote/AMZN).
   - Click on the "Historical Data" tab.
   - Set the date range to "5y" for 5 years of data.
   - Select the frequency to "Monthly."
   - Click on "Apply" and then "Download."

2. **NASDAQ Composite Data:**
   - Visit the [NASDAQ Composite page on Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC).
   - Follow the same steps as for Amazon to download 5 years of historical data with monthly increments.

Ensure that the downloaded CSV files are stored in the same directory as the provided Python scripts or update the `file_path` variables in the scripts with the correct file paths.

## Dependencies

Before running the code, make sure to install the required dependencies using the following commands:

```bash
pip install pandas matplotlib
```

# Code Overview

This project conducts a comprehensive analysis of Amazon's stock performance compared to the NASDAQ Composite index over the past 5 years. The analyses include visualizations such as a Monthly Returns Comparison, displaying the monthly returns of Amazon and NASDAQ, a visualization of Stock Prices for Amazon over 5 years, and a comparison of Monthly Returns Over Different Years. Additionally, the project features an Amazon and NASDAQ Returns Overlay for a direct comparison of their monthly returns. It calculates and prints the Average Returns for both Amazon and NASDAQ, and generates a bar plot showcasing the Monthly Returns for the NASDAQ Composite. Furthermore, the project evaluates the Average Volatility for Amazon and NASDAQ and provides a Visualization of Differences, offering insights into the average return rate and volatility disparities between Amazon and the NASDAQ Composite.

# How to Run

Each analysis has its own Python script. To run a specific analysis, use the following command:

```bash
python script_name.py
```
Replace script_name.py with the desired script from the list above.
Feel free to explore and modify the code based on your requirements.


