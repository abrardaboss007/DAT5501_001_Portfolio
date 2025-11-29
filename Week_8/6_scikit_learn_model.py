# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous forecasting activity) in order to be able to forecast using sci-kit learn
# Load data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "fertility_rates_usa.csv")
df = pd.read_csv(csv_path)
df = df.rename(columns={"Entity": "Country", "Fertility rate (period), historical": "Fertility Rate"})
usa_df = df[df["Country"] == "United States"]
usa_df["Fertility Rate"] = pd.to_numeric(usa_df["Fertility Rate"], errors="coerce")
usa_df["Year"] = pd.to_numeric(usa_df["Year"], errors="coerce")
usa_df = usa_df.dropna(subset=["Year", "Fertility Rate"]).reset_index(drop=True)

# Sort data by Year (important!)
usa_df = usa_df.sort_values("Year")

# Create lagged features
def create_lag_features(data, n_lags=3):
    df_lag = data.copy()
    for lag in range(1, n_lags + 1):
        df_lag[f'lag_{lag}'] = df_lag['Fertility Rate'].shift(lag)
    df_lag = df_lag.dropna().reset_index(drop=True)
    return df_lag

n_lags = 3
df_lagged = create_lag_features(usa_df, n_lags)

# Split into train and test based on year
train_df = df_lagged[df_lagged["Year"] < df_lagged["Year"].max() - 9]
test_df = df_lagged[df_lagged["Year"] >= df_lagged["Year"].max() - 9]

feature_cols = [f'lag_{i}' for i in range(1, n_lags + 1)]

X_train = train_df[feature_cols].values
y_train = train_df["Fertility Rate"].values

X_test = test_df[feature_cols].values
y_test = test_df["Fertility Rate"].values
# ------------------------------------------------------------------------------------------------
# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Plot results
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(train_df["Year"], train_df["Fertility Rate"], label='Training Data', color='blue')
ax.plot(test_df["Year"], y_test, label='Test Data (Actual)', color='red', marker='o', linestyle='None')
ax.plot(test_df["Year"], y_pred, label='Forecast', color='orange', marker='x')
ax.set_xlabel('Year')
ax.set_ylabel('Fertility Rate')
ax.set_title(f'Time Series Forecasting with Linear Regression (lags={n_lags})')
ax.legend()

st.pyplot(fig)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
st.write(f"Test RMSE: {rmse:.4f}")