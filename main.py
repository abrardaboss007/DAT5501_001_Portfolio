# Hey Ed, in order to run all project files, write streamlit run main.py in a new terminal

import streamlit as st

pages = {
    "Week 2": [
        st.Page("Week_2/compound_interest_calculator.py", title="Compound Interest Calculator"),
    ],
    "Week 3": [
        st.Page("Week_3/calendar_printer.py", title="Calendar Printer"),
    ],
    "Week 4": [
        st.Page("Week_4/Datetime_calculator.py", title="Datetime calculator"),
    ],
    "Weeks 5,6 and 7": [
        st.Page("Week_5/asset_prices.py", title="Asset Prices"),
        st.Page("Week_5/election_data.py", title="2016 Election Data")
    ],
    "Weeks 8 and 9": [
        st.Page("Week_8/fertility_rates_usa_fitting_forecasting.py", title="USA Fertility Rates Forecasting"),
        st.Page("Week_8/Week_8_README.py", title="Week 8 README")
    ],
        "Week 10": [
        st.Page("Week_4/example.py", title="Example"),
    ],
}

pg = st.navigation(pages)
pg.run()