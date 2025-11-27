# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import streamlit as st
import datetime
import pandas as pd
import os

# Use os module to be so CSV file can be brought in cross-platform
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "random_dates.csv")

# Bring in CSV file
df = pd.read_csv(csv_path)

todays_date= datetime.date.today()
yesterdays_date = todays_date - datetime.timedelta(days=1)
tomorrows_date = todays_date + datetime.timedelta(days=1)

# Create two columns, one for original tasks, the other for extension activity
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        input_first_date = st.date_input(label="Enter a date in the past", value=None, min_value= datetime.date(1970,1,1), max_value=yesterdays_date) # Allow user to only be able to select a past date
        input_second_date  = st.date_input(label = "Enter a date in the future", value=None, min_value=tomorrows_date, max_value=datetime.date(2070,1,1)) # Allow user to be able to only select a future date

        # If user selects a past date only, it will show the difference between todays date and past date
        # If user selects a future date only, it will show the difference between future date and todays date
        # If user selects both, it will show both as well as difference between future and past date
        if input_first_date and input_second_date:
            st.markdown(f"There are **{(todays_date - input_first_date).days}** days between today and {input_first_date}")
            st.markdown(f"There are **{(input_second_date - todays_date).days}** days between {input_second_date} and today")
            st.markdown(f"There are **{(input_second_date - input_first_date).days}** days between {input_second_date} and {input_first_date}")
        elif input_first_date:
            st.markdown(f"There are **{(todays_date - input_first_date).days}** days between today and {input_first_date}")
        elif input_second_date:
            st.markdown(f"There are **{(input_second_date - todays_date).days}** days between {input_second_date} and today")
        else:
            st.info("Hey Ed! Please fill at least one of the above in!")

# Extension activity was to calculate the difference between todays date and the random dates in the CSV file
with col2:
    with st.container(border=True):
        st.markdown("**Extension Activity**")
        
        df.columns = ["Dates"] # Rename column

        # Create separate columns for day, month, year
        df1 = df["Dates"].str.split('/', expand=True)

        merged_df = df.join(df1) # Join df1 with df
        merged_df.columns = ["Dates","Day","Month","Year"] # Name all columns

        # Get each column in a numpy array with numeric type for day, month, year
        random_dates = merged_df["Dates"].to_numpy()
        random_days = pd.to_numeric(merged_df["Day"], errors="coerce").to_numpy()
        random_months = pd.to_numeric(merged_df["Month"], errors="coerce").to_numpy()
        random_years = pd.to_numeric(merged_df["Year"], errors="coerce").to_numpy()

        for i in range(len(merged_df)):
            st.markdown(f"There are **{((todays_date) - (datetime.date(random_years[i],random_months[i],random_days[i]))).days}** days between today and {random_dates[i]}")