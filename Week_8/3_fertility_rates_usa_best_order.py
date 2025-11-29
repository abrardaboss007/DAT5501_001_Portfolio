# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous forecasting activity) in order to be able to make graph of best degree
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "fertility_rates_usa.csv")
df = pd.read_csv(csv_path)

# Rename some columns
df = df.rename(columns={"Entity": "Country", "Fertility rate (period), historical": "Fertility Rate"})

# Select only fertility rates for USA
usa_df = df[df["Country"] == "United States"]

# Convert fertility rate and year from string to numeric data type
usa_df["Fertility Rate"] = pd.to_numeric(usa_df["Fertility Rate"], errors="coerce")
usa_df["Year"] = pd.to_numeric(usa_df["Year"], errors="coerce")

# Clean dataset first - remove NaNs
usa_df = usa_df.dropna(subset=["Year", "Fertility Rate"]).reset_index(drop=True)

train_df = usa_df.iloc[0:-10]  # training data
test_df = usa_df.iloc[-10:]    # test data

x_train = train_df["Year"].to_numpy()
y_train = train_df["Fertility Rate"].to_numpy()
x_test = test_df["Year"].to_numpy()
y_test = test_df["Fertility Rate"].to_numpy()

degree = 1 # Only degree 1 this time since its the best
coeffs = np.polyfit(x_train, y_train, degree)
poly = np.poly1d(coeffs)

# Predict on training to get residuals
y_train_pred = poly(x_train)
residuals = y_train - y_train_pred

# Estimate uncertainty per point using residual stddev in a moving window
window_size = 5  # years on each side
uncertainties = []

for year in train_df["Year"]:
    # Select points within the window size
    window_mask = (train_df["Year"] >= year - window_size) & (train_df["Year"] <= year + window_size)
    window_residuals = residuals[window_mask]
    # Calculate stddev of residuals in this window, fallback to overall std if empty
    if len(window_residuals) > 1:
        uncertainties.append(np.std(window_residuals))
    else:
        uncertainties.append(np.std(residuals))

uncertainties = np.array(uncertainties)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot training data with error bars for uncertainties
ax.errorbar(x_train, y_train, yerr=uncertainties, fmt='o', markersize=5, label="Training Data with uncertainties", capsize=3)

# Plot degree 1 polynomial fit line on full range (training + test)
x_full = np.concatenate((x_train, x_test))
x_full_sorted = np.sort(x_full)
y_full_pred = poly(x_full_sorted)
ax.plot(x_full_sorted, y_full_pred, color="orange", label="Degree 1 Polynomial Fit")

# Plot test data actual points
ax.scatter(x_test, y_test, color="red", marker="o", s=30, label="Test Data (Actual)")

ax.set_xlabel("Year")
ax.set_ylabel("Fertility Rate")
ax.set_title("Fertility rates in USA with Degree 1 Polynomial Fit")
ax.set_ylim(0, 4)
ax.legend(loc='upper right')

st.pyplot(fig)
