import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Define the file path for the CSV file
file_path = os.path.join('AAPL_Stock_data.csv')

# Load CSV file
data = pd.read_csv(file_path)

# Drop duplicates and missing values
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Feature selection: Use relevant columns (adjust as needed)
features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = data[features]

# Target variable: Use 'Close' price
y = data['Close']

# Data scaling- Just Check
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
