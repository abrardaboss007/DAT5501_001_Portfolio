import streamlit as st

def blankspace():
    st.markdown("‎ ")

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
start_day = st.selectbox(label="**Starting day of the month**", options=days_of_the_week, placeholder="Select an option...")
blankspace()

no_of_days_in_month = st.slider(label="**Number of days in the month**", min_value=28, max_value=31, value=28, step=1)
blankspace()

no_days_in_the_week = 7

# Header row with border containers
columns = st.columns(no_days_in_the_week)
for i in range(no_days_in_the_week):
    with columns[i]:
        with st.container(border=True):
            st.markdown(f"**{days_of_the_week[i][0]}**")

try:
    start_index = days_of_the_week.index(start_day)

    calendar_slots = []
    for _ in range(start_index):
        calendar_slots.append("")

    for day_num in range(1, no_of_days_in_month + 1):
        calendar_slots.append(str(day_num))

    while len(calendar_slots) % 7 != 0:
        calendar_slots.append("")

    total_weeks = len(calendar_slots) // 7

    for week in range(total_weeks):
        cols = st.columns(no_days_in_the_week)
        for i in range(no_days_in_the_week):
            day_val = calendar_slots[week * 7 + i]
            with cols[i]:
                if day_val == "":
                    st.write(" ")
                else:
                    with st.container(border=True):
                        st.write(day_val)

except Exception:
    st.info("Hey Ed! Fill in the info above please!")