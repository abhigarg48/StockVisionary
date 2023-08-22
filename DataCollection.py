# Obtain 'API key' https://www.alphavantage.co/ 


# Installing Libraries (cmd)
pip install pandas
pip install numpy 
pip install scikit-learn
pip install tensorflow 
pip install alpha_vantage
pip install matplotlib

#Else Shortcut Installing Libraries (cmd)
pip install pandas numpy scikit-learn tensorflow alpha_vantage matplotlib


#Verify Install
pip show 'library name'


#Data Retrieving
import pandas as pd
from alpha_vantage.timeseries import TimeSeries


# Set your Alpha Vantage API key and stock symbol
api_key = 'API-Key'
symbol = 'AAPL' #Apple Stock Data

# Initialize Alpha Vantage API client
ts = TimeSeries(key=api_key, output_format='pandas')

# Retrieve historical daily stock price data for the past 30 years
data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
data = data.tail(30*252)  # Consider approximately 252 trading days per year
