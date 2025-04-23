# Bing COVID-19 Stock & Case Data Analysis

This project explores the relationship between daily confirmed COVID-19 cases and adjusted close stock prices for 15 publicly traded companies across healthcare, travel, e-commerce, and retail sectors.

## Datasets

### Stock Data
- Source: [Yahoo Finance](https://finance.yahoo.com/)
- Accessed via: [`yfinance`](https://github.com/ranaroussi/yfinance) Python package
- Date Range: 2020-03-16 to 2023-02-02
- Contains adjusted close prices for 15 tickers:
  - `MRNA`, `PFE`, `BNTX`, `ABT` *(Healthcare)*
  - `AMZN`, `ZM`, `PTON` *(E-commerce/Remote Work)*
  - `DAL`, `UAL`, `MAR`, `HLT`, `CCL`, `RCL` *(Travel/Hospitality)*
  - `M`, `KSS` *(Retail)*

**Download CSV:**  
[StockAdjClose_2020_2023_PandemicSensitive.csv](https://raw.githubusercontent.com/mcorosz/Bing-Covid-19-Project/main/StockAdjClose_2020_2023_PandemicSensitive.csv)

### COVID-19 Case Data
- Source: [Covid Bing dataset]
- Aggregated to daily U.S. total case counts
- Merged with stock data for time-aligned analysis

## Business Questions Explored
- How did pandemic-sensitive stocks respond to confirmed COVID-19 case surges?

## Tools Used
- Python (pandas, yfinance)
- SQL Server
- Power BI for interactive dashboards

## Notes
- All analysis performed on publicly available data
- Daily granularity allows for time series forecasting and correlation analysis
