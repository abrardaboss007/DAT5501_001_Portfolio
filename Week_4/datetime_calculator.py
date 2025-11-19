import streamlit as st
import datetime

todays_date= datetime.date.today()
yesterdays_date = todays_date - datetime.timedelta(days=1)
tomorrows_date = todays_date + datetime.timedelta(days=1)

input_first_date = st.date_input(label="Enter a date in the past", value=None, min_value= datetime.date(1970,1,1), max_value=yesterdays_date)

input_second_date  = st.date_input(label = "Enter a date in the future", value=None, min_value=tomorrows_date, max_value=datetime.date(2070,1,1))


if input_first_date and input_second_date:
    st.write(f"There are **{(todays_date - input_first_date).days}** days between today and {input_first_date}")
    st.write(f"There are **{(input_second_date - todays_date).days}** days between {input_second_date} and today")
    st.write(f"There are **{(input_second_date - input_first_date).days}** days between {input_second_date} and {input_first_date}")
elif input_first_date:
    st.write(f"There are **{(todays_date - input_first_date).days}** days between today and {input_first_date}")
elif input_second_date:
    st.write(f"There are **{(input_second_date - todays_date).days}** days between {input_second_date} and today")
else:
    st.info("Hey Ed! Please fill the above in!")


