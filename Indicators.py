import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np

# Declaring a start time of one year ago
start = dt.datetime.today()-dt.timedelta(days=365)


def roc_nasdaq():
    # Pulling Nasdaq data from Yahoo finance
    df_nasdaq = web.DataReader('^IXIC', 'yahoo', start=start)

    # This will be used to turn the pulled data into a csv for storage
    # and quick access
    # df_nasdaq.to_csv('nasdaq.csv')
    # stored_df_nasdaq = pd.read_csv('Nasdaq.csv', parse_dates= True, index_col=0)

    # Turns the Adjusted Closing price column into an array
    nasdaq_array = df_nasdaq['Adj Close'].values

    # Calculates ratio between most recent Adjusted Closing price and 1 year ago
    calc_roc_nasdaq = (nasdaq_array[-1]/nasdaq_array[1])

    # Prints results
    print(calc_roc_nasdaq)


def roc_sp500():
    # Pulling S&P 500 data from Yahoo finance
    df_sp500 = web.DataReader('^GSPC', 'yahoo', start=start)

    # This will be used to turn the pulled data into a csv for storage
    # and quick access
    # df_sp500.to_csv('sp500.csv')
    # stored_df_sp500 = pd.read_csv('sp500.csv', parse_dates= True, index_col=0)

    # Turns the Adjusted Closing price column into an array
    sp_array = df_sp500['Adj Close'].values

    # Calculates ratio between most recent Adjusted Closing price and 1 year ago
    calc_roc_sp500 = (sp_array[-1] / sp_array[1])

    # Prints result
    print(calc_roc_sp500)


def roc_dji():
    # Pulling Dow Jones Industrial Average data from Yahoo finance
    df_dji = web.DataReader('^DJI', 'yahoo', start=start)

    # This will be used to turn the pulled data into a csv for storage
    # and quick access
    # df_dji.to_csv('dji.csv')
    # stored_df_dji = pd.read_csv('dji.csv', parse_dates= True, index_col=0)

    # Turns the Adjusted Closing price column into an array
    dji_array = df_dji['Adj Close'].values

    # Calculates ratio between most recent Adjusted Closing price and 1 year ago
    calc_roc_dji = (dji_array[-1] / dji_array[1])

    # Prints results
    print(calc_roc_dji)


def google_stochastic():
    # Declaring a start time 14 days ago
    so_start = dt.datetime.today() - dt.timedelta(days=14)

    # Pulling Google stock data from Yahoo finance
    df_goog = web.DataReader('GOOG', 'yahoo', so_start)

    # This will be used to turn the pulled data into a csv for storage
    # and quick access
    # df_Goog.to_csv('Goog.csv')
    # stored_df_Goog = pd.read_csv('Goog.csv', parse_dates = True, index_col=0)

    # Converts the Closing price column, daily high price, and daily low price into arrays
    goog_close_array = df_goog['Close']
    goog_high_array = df_goog['High'].values
    goog_low_array = df_goog['Low'].values

    # Finds the most recent closing price, and the highest and lowest price over the period
    goog_close = goog_close_array[-1]
    high = np.max(goog_high_array)
    low = np.min(goog_low_array)

    # Calculates 14 day trading period Stochastic Oscillator
    stochastic_oscillator = ((goog_close-low)/(high-low))

    # Prints results
    print(stochastic_oscillator)
