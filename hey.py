import streamlit as st
#----------------------------------------------------------------------------------
# Introduction
st.title("Hey Ed!")

st.markdown("""
            If you're reading this before having run any of the activities, please note
            that the way to view the pages is by typing **streamlit run main.py** on a new terminal.
            If you want to run the unit tests, then simply click on a new terminal 
            and type **pytest**""")

st.markdown("""Anyways the purpose of this page is simply to give a brief refresher of each task
            and my approach to each one""")
#----------------------------------------------------------------------------------
# Week 1
st.title("Week 1")
st.markdown("Pretty simple week")
st.markdown("I created a program which prints hello world")
st.markdown("I also created a function which prints the n'th triangular number with unit tests as well for it")
st.markdown("P.S: A triangular number is a number that can be represented by a triangle of dots, where each row has one more dot than the row above it")

#----------------------------------------------------------------------------------
# Week 2
st.title("Week 2")
st.markdown("This is when things started to slightly ramp up, hence I began using a UI for my activities (streamlit)")

st.markdown("""For week 2, the tasks was to ask the user to input his initial savings amount, the amount
            of interest he was accruing per year, and the number of years he planned accruing interest
            on the savings. It would then tell the user his savings amount after each year and the number
            of years it would take for him to double his savings""")

st.markdown("""The default savings amount when you click on the page is 1000.00,
            The default interest rate is 10.00
            and the default number of years is 1.
            However, these can all be changed by interacting with the page.
            For the first two, you do not need to press the + or - buttons,
            you can simply click on the box and type a number in if you wish""")

st.markdown("""Since my activity is UI based, a lot of my tests were based on ensuring the inputs like
            number input and slider functioned as intended. This was done by importing streamlit's App testing.
            This kind of testing will continue on throughout the other tests I do in future weeks""")

#----------------------------------------------------------------------------------
# Week 3
st.title("Week 3")
st.markdown("Week 3 was the calendar printer task")
st.markdown("The task was to have headers displaying")
st.markdown("'S M T W T F S'")
st.markdown("""and also to ask the user the start day of the week and how many days there
            are in this month""")
st.markdown("A calendar would be printed accordingly")
st.markdown("Again, tests mainly revolved around ensuring that the buttons functioned as intended")

#----------------------------------------------------------------------------------
# Week 4
st.title("Week 4")
st.markdown("""I created a date time calculator wherein the first half of the activity was to ask 
            the user for a date and the number of days between today's date and the inputted date
            would be generated. I put a little spin on this project by asking the user to put in
            two dates, one from the past and one in the future (i added code to ensure they would
            not be able to circumnavigate this) and then it would output the difference between the future
            date and todays date, the difference between todays date and the past date and the difference
            between the future and past date. If the user filled in only one of the date inputs, the 
            output would be accordingly""")
st.markdown("""The extension activity was to calculate the difference between random dates within a CSV
            file and today's date which was done on a separate columns""")
st.markdown("Unit tests have also be completed for this activity")

#----------------------------------------------------------------------------------
# Weeks 5,6,7
st.title("Week 5,6 and 7")
st.markdown("There were two activities here")

st.markdown("""The first was to generate the close price for the previous year of a particular asset.
            I wanted to extend this further and give the user some variety. Hence I allowed the user
            to be able to input the ticker symbol of any US stock and it would generate the close price
            for the previous year of that stock. Then suddenly, this API company started to introduce 
            free and paid version during around the time I was using this. Hence, the free version
            only allows me to be able to view close price data for around the last 5 months, so the
            graph can only be close prices for the last 5 months now.""")

st.markdown("Then, as part of the extension activity, I made the daily percentage change graph for that stock")

st.markdown("The standard deviaton of the daily percentage change as well as the average open and close prices in that period can be viewed as well")
st.markdown("""Finally, as part of an extra extension that was assigned on week 8 Monday (which I am 
            adding in Week 5 just because I think it makes most sense to) I also computed the time complexity of sorting the 
            daily price changes""")

st.markdown("All of these activities can be viewed on the same page")

st.markdown("The second activity was the US election data task")

st.markdown("""For this task, we were supposed to select a particular candidate of our choice, 
            then plot a histogram of the fraction of votes for that candidate in each state. 
            I extended this further and allowed the user to select the candidate, hence
            the graph would be updated accordingly""")

st.markdown("""The extension was to then compare the votes for two candidates in each state.
            I again extended this and allowed the user to choose the second candidate""")

st.markdown("The unit tests are available as well")

st.markdown("There were NO activites for week 6 or week 7 due to holidays and sprint week respectively")
#----------------------------------------------------------------------------------
# Weeks 8,9
st.title("Weeks 8 and 9")

st.markdown("For week 8, the Monday task can be seen on week 5") 

st.markdown("""The newest activity after that was to find a dataset for the last 100 years. I chose to use fertility rates in the USA 
            The inital task for this activity was to the subsample all but the last 10 years. Then 
            use polynomials of degree 1 to 9 to see which degree was closest to the true values 
            of the last 10 years. The second part of this activity was to calculate and plot
            the chi squared per degree of freedom and the Bayesian Information Criterion 
            as a function of the polynomial. From this, it would be able to be deduced which
            polynomial model is the best. Then, with the best polynomial model, we could calculate
            the parameter values (and their uncertainties) as well as the covariance matrix. I then
            came up with a model which I considered to be better which was the Gaussian Model""")

st.markdown("""As part of an extension activity, I used the emcee module in Python to see if it could make
            more accurate predictions. I also gave myself an extension activity, which was to use the
            sci-kit learn module instead""")

st.markdown("""It should be noted this work encompasses both Week 8 and 9""")
#----------------------------------------------------------------------------------
# Week 10
st.title("Week 10")