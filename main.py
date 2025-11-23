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
    "Week 5": [
        st.Page("Week_5/asset_prices.py", title="Asset Prices"),
        st.Page("Week_5/election_data.py", title="2016 Election Data")
    ],
    "Week 8": [
        st.Page("Week_8/fertility_rates_usa_fitting_forecasting.py", title="USA Fertility Rates Forecasting"),
    ],
}

pg = st.navigation(pages)
pg.run()