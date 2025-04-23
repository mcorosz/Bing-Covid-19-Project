"""
covid_stock_data.py

Script to download daily adjusted close prices for pandemic-sensitive stocks 
from Yahoo Finance using the yfinance API.

Date range: 2020-03-16 to 2023-02-02
Tickers: MRNA, PFE, BNTX, ABT, AMZN, ZM, PTON, DAL, UAL, MAR, HLT, CCL, RCL, M, KSS

Author: Michael Orosz
"""

import yfinance as yf
import pandas as pd

tickers = [
    'MRNA', 'PFE', 'BNTX', 'ABT', 'AMZN', 'ZM', 'PTON',
    'DAL', 'UAL', 'MAR', 'HLT', 'CCL', 'RCL', 'M', 'KSS'
]

start_date = '2020-03-16'
end_date = '2023-02-02'

adj_close = pd.DataFrame()
failed = []

for ticker in tickers:
    try:
        print(f"Downloading: {ticker}")
        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
        if 'Adj Close' in df.columns:
            adj_close[ticker] = df['Adj Close']
        else:
            raise KeyError("'Adj Close' not found in columns.")
    except Exception as e:
        print(f"Failed for {ticker}: {e}")
        failed.append(ticker)

print("\nDownload complete.")
print("Failed tickers:", failed)

adj_close.to_csv('StockAdjClose_2020_2023_PandemicSensitive.csv')
print("Data saved to 'StockAdjClose_2020_2023_PandemicSensitive.csv'")
