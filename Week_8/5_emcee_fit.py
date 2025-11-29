# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import streamlit as st
import emcee
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous forecasting activity) in order to be able to use emcee module
# Load data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "fertility_rates_usa.csv")
df = pd.read_csv(csv_path)
df = df.rename(columns={"Entity": "Country", "Fertility rate (period), historical": "Fertility Rate"})
usa_df = df[df["Country"] == "United States"]
usa_df["Fertility Rate"] = pd.to_numeric(usa_df["Fertility Rate"], errors="coerce")
usa_df["Year"] = pd.to_numeric(usa_df["Year"], errors="coerce")
usa_df = usa_df.dropna(subset=["Year", "Fertility Rate"]).reset_index(drop=True)
train_df = usa_df.iloc[0:-10]
test_df = usa_df.iloc[-10:]

x_train = train_df["Year"].to_numpy()
y_train = train_df["Fertility Rate"].to_numpy()
x_test = test_df["Year"].to_numpy()
y_test = test_df["Fertility Rate"].to_numpy()

# ------------------------------------------------------------------------------------------------
# Emcee module 
st.title("Bayesian Polynomial Fit using emcee")

nwalkers = 50
nsteps = 3000
burn_in = 1000

# Helper functions for the polynomial model and log prob
def poly_model(theta, x):
    degree = len(theta) - 1  # last param is log_sigma
    coeffs = theta[:-1]
    y = np.polyval(coeffs, x)
    return y

def log_prior(theta):
    coeffs = theta[:-1]
    log_sigma = theta[-1]
    # Uniform priors for coefficients -5 to 5
    if np.all((-5 < coeffs) & (coeffs < 5)) and (-10 < log_sigma < 1):
        return 0.0
    else:
        return -np.inf

def log_likelihood(theta, x, y):
    log_sigma = theta[-1]
    sigma = np.exp(log_sigma)
    model_pred = poly_model(theta, x)
    return -0.5 * np.sum(((y - model_pred) / sigma) ** 2 + np.log(2 * np.pi * sigma ** 2))

def log_posterior(theta, x, y):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y)

degree = 1
st.header(f"Degree {degree} polynomial")

ndim = degree + 2  # polynomial coeffs + log_sigma
# Least squares initial guess
coeffs_ls = np.polyfit(x_train, y_train, degree)
log_sigma_init = np.log(np.std(y_train - np.polyval(coeffs_ls, x_train)))
starting_guesses = np.append(coeffs_ls, log_sigma_init)
pos = starting_guesses + 1e-4 * np.random.randn(nwalkers, ndim)

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x_train, y_train))
sampler.run_mcmc(pos, nsteps, progress=True)

samples = sampler.get_chain(discard=burn_in, flat=True)

# Predict on test data, sampling predictive distribution
pred_samples = []
for sample in samples:
    pred_samples.append(np.polyval(sample[:-1], x_test))
pred_samples = np.array(pred_samples)

pred_mean = np.mean(pred_samples, axis=0)
pred_std = np.std(pred_samples, axis=0)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x_train, y_train, label="Training Data", color="blue", s=20)
ax.scatter(x_test, y_test, label="Test Data", color="red", s=30)
ax.plot(x_test, pred_mean, color="orange", label="Mean Prediction (MCMC)")
ax.fill_between(x_test, pred_mean - pred_std, pred_mean + pred_std,
                color="orange", alpha=0.3, label="Prediction uncertainty")
ax.set_xlabel("Year")
ax.set_ylabel("Fertility Rate")
ax.set_title(f"Degree {degree} Polynomial Bayesian Fit with emcee")
ax.legend(loc='upper left')
st.pyplot(fig)

# Root mean square error
rmse = np.sqrt(np.mean((y_test - pred_mean) ** 2))
st.write(f"Degree {degree} RMSE on test data: {rmse:.4f}")