import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Define the file path for the CSV file
file_path = os.path.join('AAPL_historical_data.csv')

# Load CSV file
data = pd.read_csv(file_path)
