# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.dates as mdates
import seaborn as sns
import requests
import time

api_key = "BYHB2K7TAGFZ3ESE"

symbol = st.text_input(label="Enter the **ticker symbol** of a **US** stock", placeholder=  f"e.g. AAPL", max_chars=5, value=None)

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&datatype=csv&apikey={api_key}'

col1, col2 = st.columns(2)

try:
    with col1:
        # Display graph for stock
        df = pd.read_csv(url)
        last_year_df = df.head(n=100) # only data is available for the last 5 months in the free version of the API now
        last_year_df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        
        # change open and close columns to numeric data type
        last_year_df["close"] = pd.to_numeric(df["close"], errors="coerce")
        last_year_df["open"] = pd.to_numeric(df["open"],errors="coerce")

        x_values = last_year_df["timestamp"].to_numpy()
        y_values_close_prices = last_year_df["close"].to_numpy()

        fig1, ax1 = plt.subplots()
        ax1.plot(x_values, y_values_close_prices, linestyle="-", color="blue", linewidth= 2)

        ax1.set_title(f"Closing price vs. date of {symbol} for last year")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Closing Price")
        st.pyplot(fig1)

    with col2:
        # Display daily percentage change for stock
        y_values_daily_percentage_change = ((-np.diff(y_values_close_prices)) / y_values_close_prices[:-1] * 100 )
        
        fig2, ax2 = plt.subplots()
        ax2.plot(x_values[:-1],y_values_daily_percentage_change, linestyle="-", color="red")
        ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1))
        
        ax2.set_title(f"Daily percentage change vs. date of {symbol} for last year")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Daily Percentage Change")
        st.pyplot(fig2)

except Exception as e:
    st.info("Oops, something went wrong Ed! Are you sure everything above is filled in?")


col3,col4 = st.columns(2)

try:
    with col3:
        # Plot graph of Time complexity against n log n
        # Calculate daily price changes Ap = Pn+1 - Pn
        daily_change_prices = np.diff(y_values_close_prices)

        daily_change_sample_size = np.arange(7, len(daily_change_prices) + 1, 1)  # from 7 up to length(Ap) step 1
        times = []

        for n in daily_change_sample_size:
            data = daily_change_prices[:n]
            start = time.time()
            sorted_data = sorted(data)
            end = time.time()
            times.append(end - start)


        fig3, ax3 = plt.subplots()
        ax3.plot(daily_change_sample_size, times, label='Sorting Time T(n)')
        
        # scale n log n to best fit last point
        scale_factor = times[-1] / (daily_change_sample_size[-1] * np.log2(daily_change_sample_size[-1]))
        ax3.plot(daily_change_sample_size, daily_change_sample_size * np.log2(daily_change_sample_size) * scale_factor, label='Scaled n log n')

        ax3.set_xlabel('Input Size (n)')
        ax3.set_ylabel('Time (seconds)')
        ax3.set_title('Time Complexity of Sorting Daily Price Changes')
        ax3.legend()
        ax3.grid(True)
        st.pyplot(fig3)

    with col4:
        # Display standard deviation of daily percentage change as well as mean open and close prices in time period
        standard_deviation = np.std(y_values_daily_percentage_change)
        mean_open_price = last_year_df["open"].mean()
        mean_close_price = last_year_df["close"].mean()
        st.markdown(f"Standard deviation of daily percentage change: **{round(standard_deviation,2)}**")
        st.markdown(f"{symbol}'s mean open price: **{round(mean_open_price,2)}**")
        st.markdown(f"{symbol}'s mean close price: **{round(mean_close_price,2)}**")

except Exception as e:
    st.markdown("‎")