# # Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

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

# train_df = usa_df.iloc[0:-10] # Select 1933 to 2013 (training data)
# test_df = usa_df.iloc[-10:] # Select 2014 to 2023 (testing data)

# x_values_training = train_df["Year"].to_numpy()
# y_values_training = train_df["Fertility Rate"].to_numpy()

# fig1, ax1 = plt.subplots()
# ax1.scatter(x_values_training, y_values_training, marker="o", s=10)

# all_predictions = {}
# for degree in range(1, 10):
#     coeffs,cov = np.polyfit(x_values_training, y_values_training, deg=degree, cov= True)
#     st.write(f"Degree {degree} Coefficients:", coeffs)
#     #st.write(f"Cov for {degree}", cov)

#     # Create polynomial function from coefficients
#     poly = np.poly1d(coeffs)

#     # Predict fertility rates on test years
#     x_test = test_df["Year"].to_numpy()
#     y_pred = poly(x_test)
#     all_predictions[degree] = y_pred

#     # Plot prediction for test years with line or scatter for visibility
#     ax1.plot(x_test, y_pred, label=f"Degree {degree} Prediction")
#     #ax1.legend(loc='right', bbox_to_anchor=(1, 0.5), fontsize='small')
# # Plot actual test data points for comparison
# ax1.scatter(test_df["Year"], test_df["Fertility Rate"], color="red", marker="o", s=10, label="Test Data (Actual)")
# ax1.set_ylim(0,4)
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Fertility Rate")
# ax1.set_title("Fertility rates in USA with Polynomial Forecasts")
# ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
# st.pyplot(fig1)

# # Optionally show errors (RMSE) for each degree to compare quality
# st.subheader("Forecast RMSE (Test Set)")
# for degree in range(1, 10):
#     y_true = test_df["Fertility Rate"].to_numpy()
#     y_pred = all_predictions[degree]
#     rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
#     st.write(f"Degree {degree}: RMSE = {rmse:.4f}")


# Clean dataset first - remove NaNs
usa_df = usa_df.dropna(subset=["Year", "Fertility Rate"])

train_df = usa_df.iloc[0:-10] # training data
test_df = usa_df.iloc[-10:] # test data

x_values_training = train_df["Year"].to_numpy()
y_values_training = train_df["Fertility Rate"].to_numpy()

all_predictions = {}
fig1, ax1 = plt.subplots()
ax1.scatter(x_values_training, y_values_training, marker="o", s=10)

for degree in range(1, 10):
    if len(x_values_training) <= degree:
        st.write(f"Skipping degree {degree} because not enough points for fitting")
        continue
    coeffs= np.polyfit(x_values_training, y_values_training, deg=degree)
    st.write(f"Degree {degree} Coefficients:", coeffs)
    #st.write(f"Covariance matrix for degree {degree}:", cov)

    poly = np.poly1d(coeffs)

    x_test = test_df["Year"].to_numpy()
    y_pred = poly(x_test)
    all_predictions[degree] = y_pred

    ax1.plot(x_test, y_pred, label=f"Degree {degree} Prediction")

ax1.scatter(test_df["Year"], test_df["Fertility Rate"], color="red", marker="o", s=10, label="Test Data (Actual)")
ax1.set_ylim(0, 4)
ax1.set_xlabel("Year")
ax1.set_ylabel("Fertility Rate")
ax1.set_title("Fertility rates in USA with Polynomial Forecasts")
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')

st.pyplot(fig1)

# RMSE calculations as before
st.subheader("Forecast RMSE (Test Set)")
for degree in range(1,10):
    y_true = test_df["Fertility Rate"].to_numpy()
    y_pred = all_predictions[degree]
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    st.write(f"Degree {degree}: RMSE = {rmse:.4f}")

# Best fit is degree one 

import matplotlib.pyplot as plt

chi2_per_dof_vals = []
bic_vals = []
degrees = []

y_true = test_df["Fertility Rate"].to_numpy()
n = len(y_true)

for degree, y_pred in all_predictions.items():
    k = degree + 1  # number of parameters
    residuals = y_true - y_pred
    RSS = np.sum(residuals ** 2)
    
    dof = n - k
    chi2_per_dof = RSS / dof if dof > 0 else np.nan
    
    bic = n * np.log(RSS / n) + k * np.log(n)
    
    degrees.append(degree)
    chi2_per_dof_vals.append(chi2_per_dof)
    bic_vals.append(bic)
    
# Plot
fig2, ax2 = plt.subplots()
ax2.plot(degrees, chi2_per_dof_vals, marker='o', label='Chi² per DoF')
ax2.plot(degrees, bic_vals, marker='s', label='BIC')
ax2.set_xlabel('Polynomial Degree')
ax2.set_title('Chi² per DoF and BIC by Polynomial Degree')
ax2.legend()
st.pyplot(fig2)

best_index = np.argmin(bic_vals)
best_degree = degrees[best_index]
st.write(f"Best polynomial degree by BIC: {best_degree}")

# Use training data to fit best model and get covariance
mask = (~np.isnan(x_values_training)) & (~np.isnan(y_values_training)) & (~np.isinf(x_values_training)) & (~np.isinf(y_values_training))
x_fit = x_values_training[mask]
y_fit = y_values_training[mask]

coeffs, cov = np.polyfit(x_fit, y_fit, deg=best_degree, cov=True)
st.write(f"Best model coefficients for degree {best_degree}:", coeffs)
st.write(f"Covariance matrix:\n", cov)

# Parameter uncertainties are the sqrt of diagonal cov elements
param_uncertainties = np.sqrt(np.diag(cov))
st.write(f"Uncertainties in parameters:", param_uncertainties)

from scipy.optimize import curve_fit

# Define exponential function
def exp_func(x, a, b):
    return a * np.exp(b * x)

# Filter training data (positive y only for log transform)
mask_exp = (y_fit > 0)
x_exp = x_fit[mask_exp]
y_exp = y_fit[mask_exp]

# Fit curve
try:
    popt, pcov = curve_fit(exp_func, x_exp, y_exp)
    st.write("Exponential model parameters:", popt)
    st.write("Covariance matrix of exponential fit:\n", pcov)
    
    # Predict on test set
    x_test = test_df["Year"].to_numpy()
    y_exp_pred = exp_func(x_test, *popt)
    
    # Plot along with polynomial fits
    fig3, ax3 = plt.subplots()
    ax3.scatter(x_fit, y_fit, label='Training Data')
    ax3.scatter(test_df["Year"], test_df["Fertility Rate"], color='red', label='Test Data')
    ax3.plot(x_test, y_exp_pred, label='Exponential Fit', color='green')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Fertility Rate')
    ax3.set_title('Exponential Model Fit')
    ax3.legend()
    st.pyplot(fig3)
    
    # RMSE for exponential fit
    y_true = test_df["Fertility Rate"].to_numpy()
    rmse_exp = np.sqrt(np.mean((y_true - y_exp_pred) ** 2))
    st.write(f"Exponential fit RMSE on test data: {rmse_exp:.4f}")
except Exception as e:
    st.error(f"Exponential fit failed: {e}")