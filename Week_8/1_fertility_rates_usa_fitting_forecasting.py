# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

# Load file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "fertility_rates_usa.csv")
df = pd.read_csv(csv_path)

# Rename some columns
df = df.rename(columns={"Entity": "Country", "Fertility rate (period), historical": "Fertility Rate"})

# Select only fertility rates for USA
usa_df = df[df["Country"] == "United States"]

# Change fertility rate and year from string to numeric data type
usa_df["Fertility Rate"] = pd.to_numeric(usa_df["Fertility Rate"], errors="coerce")
usa_df["Year"] = pd.to_numeric(usa_df["Year"], errors="coerce")

# Clean dataset first - remove NaNs
usa_df = usa_df.dropna(subset=["Year", "Fertility Rate"])

train_df = usa_df.iloc[0:-10] # training data
test_df = usa_df.iloc[-10:] # test data

x_values_training = train_df["Year"].to_numpy() 
y_values_training = train_df["Fertility Rate"].to_numpy()

all_predictions = {}
fig1, ax1 = plt.subplots()
ax1.scatter(x_values_training, y_values_training, marker="o", s=10) # Plot scatter points for training data

for degree in range(1, 10):
    # Obtain coefficients for each degree
    coeffs= np.polyfit(x_values_training, y_values_training, deg=degree)
    poly = np.poly1d(coeffs)

    x_test = test_df["Year"].to_numpy()
    y_pred = poly(x_test) # Line fitting based on x_test values
    all_predictions[degree] = y_pred 

    ax1.plot(x_test, y_pred, label=f"Degree {degree} Prediction") # Plot predicted lines for polynomial degrees 1 to 9

ax1.scatter(test_df["Year"], test_df["Fertility Rate"], color="red", marker="o", s=10, label="Test Data (Actual)") # Plot scatter points for test data
ax1.set_ylim(0, 4)
ax1.set_xlabel("Year")
ax1.set_ylabel("Fertility Rate")
ax1.set_title("Fertility rates in USA with Polynomial Forecasts")
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small') # Place legend on the side of the graph

st.pyplot(fig1)

# RMSE calculations
st.subheader("Forecast Root Mean Square Error (RMSE)")
cols = st.columns(9)
for degree in range(1,10):
    with cols[degree -1]:
        y_true = test_df["Fertility Rate"].to_numpy()
        y_pred = all_predictions[degree]
        rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
        st.write(f"Degree {degree}: RMSE = {rmse:.4f}")