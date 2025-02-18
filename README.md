# Stock Analysis and Visualization

This project analyzes and visualizes stock data for SPY (S&P 500 ETF) and GOOG (Google/Alphabet) using Python. It demonstrates various data analysis techniques and visualization methods using popular libraries such as pandas, numpy, matplotlib, and seaborn.

## Features

- Fetches historical stock data using yfinance
- Calculates logarithmic returns
- Computes correlation matrix between stocks
- Performs linear regression analysis
- Visualizes stock price trends and scatter plots

## Dependencies

- numpy
- pandas
- pandas_datareader
- matplotlib
- seaborn
- yfinance

## Usage

1. Install the required dependencies:
2. Run the script to generate visualizations and analysis:

## Visualizations

The script generates several visualizations:

1. Scatter plot of SPY vs GOOG returns with a linear regression line
2. Time series plot of SPY (S&P 500) closing prices with a trend line
3. Seaborn regression plot for the last 63 days of SPY data

## Analysis

The script performs the following analyses:

- Calculates correlation matrix between SPY and GOOG returns
- Fits a linear regression model to the sampled data
- Predicts future stock prices based on the regression model

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features.

## License

This project is open-source and available under the MIT License.
