# Hey Ed, in order to run all project files, write streamlit run main.py in a new terminal

import streamlit as st

pages = {
    "Before you check other pages...": [
        st.Page("hey.py", title="READ THIS!"),
    ],
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
        st.Page("Week_8/1_fertility_rates_usa_fitting_forecasting.py", title="USA Fertility Rates Forecasting"),
        st.Page("Week_8/2_fertility_rates_usa_dof_bic.py", title="DOF and BIC graphs"),
        st.Page("Week_8/3_fertility_rates_usa_best_order.py", title="Best Order Model"),
        st.Page("Week_8/4_gaussian_model_fitting.py", title="Gaussian Fit"),
        st.Page("Week_8/5_emcee_fit.py", title="Using emcee module"),
        st.Page("Week_8/6_scikit_learn_model.py", title="Forecasting with sci-kit learn")
    ],
        "Week 10": [
        st.Page("Week_10/decision_tree.py", title="Decision Tree"),
        st.Page("Week_10/varying_depth.py", title="Varying Depth and Feature importance")
    ],
}

pg = st.navigation(pages)
pg.run()