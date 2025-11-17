import streamlit as st
from math import log

# Create a formula that obtains savings amount, an annual interest rate, number of years and outputs the value of the 
# savings account after each year as well as how many years it would take for the savings to double
def compound_interest_calculator(savings:float, interest:float, years:int) -> float: # Cannot assume the years output to be an integer

    try:
        # Convert the user interest rate input from to a multiplier rate in decimal form
        interest_multiplier_rate = 1 + (interest/100)
        # Equation that can calculate how long it will take for savings amount to double
        years_to_double = log(2)/log(interest_multiplier_rate)
    except (UnboundLocalError, TypeError, ValueError) as e:
        st.info("Hey Ed! Please fill in the boxes **above**")
        return
    year = 0
    for i in range(years):
        # Calculate savings amount after each within the specified range
        savings *= interest_multiplier_rate
        year += 1
        st.markdown(f"Savings after year {year}: **{round(savings,2)}**")

    st.markdown(f"It will take **{round(years_to_double,2)}** years to double your money")
    return

# User inputs
savings_amount = st.number_input(label= "What is your total savings amount?", min_value=0.01, value = 1000.00, format="%0.2f", placeholder="e.g. 5000.00")
interest_rate_percentage = st.number_input(label= "What is the interest rate you are accruing annually **(as a percentage)?**", min_value=0.01, value = 10.00, format="%0.2f", placeholder="e.g. 12.87")
years_input =  st.slider(label= "How many years are you planning on keeping your money in the bank?", min_value=1, max_value=100, step=1, value=1)

compound_interest_calculator(savings= savings_amount, interest= interest_rate_percentage, years= years_input)