import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import streamlit as st
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous forecasting activity) in order to be able to make Gaussian graph
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
# ------------------------------------------------------------------------------------------------

# Perhaps Gaussian graph can be a better model considering the risk and fall between 1940-70
def gaussian(x, a, b, c, d):
    return a * np.exp(-((x - b) ** 2) / (2 * c ** 2)) + d # Gaussian Function

# Prepare data
x_data = usa_df["Year"].to_numpy()
y_data = usa_df["Fertility Rate"].to_numpy()

# Fill in parameters a, b, c, d
initial_guess = [3, 1960, 15, 1.5]  

# Fit Gaussian
params, covariance = curve_fit(gaussian, x_data, y_data, p0=initial_guess)

# Extract fitted parameters
a_fit, b_fit, c_fit, d_fit = params

print(f"Fitted parameters: a={a_fit:.3f}, b={b_fit:.1f}, c={c_fit:.3f}, d={d_fit:.3f}")

# Create figure and axes
fig, ax = plt.subplots(figsize=(20,10))

# Scatter plot of data points
ax.scatter(x_data, y_data, label="Data")

# Line plot of Gaussian fit
x_fit = np.linspace(x_data.min(), x_data.max(), 200)
y_fit = gaussian(x_fit, *params)
ax.plot(x_fit, y_fit, color='red', label="Gaussian Fit")

# Set labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Fertility Rate")
ax.set_title("Fertility Rate with Gaussian Fit")

ax.legend(loc='upper right')

# Adjust layout to make room for legend
fig.subplots_adjust(right=0.75)

st.pyplot(fig)