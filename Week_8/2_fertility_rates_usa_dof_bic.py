# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous forecasting activity) in order to be able to make DoF and BIC graphs
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
for degree in range(1, 10):
    coeffs= np.polyfit(x_values_training, y_values_training, deg=degree)
    poly = np.poly1d(coeffs)

    x_test = test_df["Year"].to_numpy()
    y_pred = poly(x_test) 
    all_predictions[degree] = y_pred
# ------------------------------------------------------------------------------------------------
# Variables that will help in plotting the graph
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
    
col1, col2 = st.columns(2)
with col1:
    # Plot Chi2 per DoF and BIC by polynomial degree on same graph
    fig2, ax2 = plt.subplots()
    ax2.plot(degrees, chi2_per_dof_vals, marker='o', label='Chi² per DoF')
    ax2.plot(degrees, bic_vals, marker='s', label='BIC')
    ax2.set_xlabel('Polynomial Degree')
    ax2.set_title('Chi² per DoF and BIC by Polynomial Degree')
    ax2.legend()
    st.pyplot(fig2)

    # Inform user of best model
    best_index = np.argmin(bic_vals)
    best_degree = degrees[best_index]
    st.write(f"Best polynomial degree by BIC: {best_degree}")


with col2:
    # Inform user of coefficient of best model and uncertainties in parameters
    mask = (~np.isnan(x_values_training)) & (~np.isnan(y_values_training)) & (~np.isinf(x_values_training)) & (~np.isinf(y_values_training))
    x_fit = x_values_training[mask]
    y_fit = y_values_training[mask]

    coeffs, cov = np.polyfit(x_fit, y_fit, deg=best_degree, cov=True)
    st.write(f"Model coefficients for degree {best_degree}:", coeffs)
    st.write(f"Covariance matrix:\n", cov)

    # Parameter uncertainties are the sqrt of diagonal cov elements
    param_uncertainties = np.sqrt(np.diag(cov))
    st.write(f"Uncertainties in parameters:", param_uncertainties)
