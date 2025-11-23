import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "US-2016-primary.csv")
df = pd.read_csv(csv_path, sep = ";")

# df1 = df.groupby(["candidate", "state"])[["votes", "fraction_votes"]].sum()
# df2 = df.groupby(["state", "candidate"])[["votes", "fraction_votes"]].sum()

candidates_list = df["candidate"].unique().tolist()
df["votes"] = pd.to_numeric(df["votes"],errors="coerce")
df["fraction_votes"] = pd.to_numeric(df["fraction_votes"],errors="coerce")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        compare_candidates_option = st.toggle(label="Compare the vote fraction for two candidates", value=False)

with col2:
    with st.container(border=True):
        if compare_candidates_option:
            first_candidate_option = st.selectbox(label="Select first candidate", options=candidates_list, index=None, placeholder="Click to select...")
            try:
                first_candidate_df = df[df["candidate"] == first_candidate_option]
            except Exception as e:
                st.warning("Hey Ed! Please select first candidate above please!")
            with col3:
                with st.container(border=True):
                    second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
                    second_candidate_option = st.selectbox(label="Select second candidate", options=second_candidate_options, index=None, placeholder="Click to select...")
                    try:
                        second_candidate_df = df[df["candidate"] == second_candidate_option]
                    except Exception as e:
                        st.warning("Hey Ed! Please select second candidate above please!")
        else:
            first_candidate_option = st.selectbox(label="Select candidate", options=candidates_list, index=None, placeholder="Click to select...")
            try:
                first_candidate_df = df[df["candidate"] == first_candidate_option]
            except Exception as e:
                st.warning("Hey Ed! Please select candidate name above please!")

# with col3:
#     if compare_candidates_option:
#         with st.container(border=True):
#             second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
#             second_candidate_option = st.selectbox(label="Select second candidate", options=second_candidate_options, index=None, placeholder="Click to select...")

#incorporate option that removes the option that user selected first
# if first_candidate_optio:
#     df1 = df[df["candidate"] == first_candidate_option]



st.write(df)
st.write(first_candidate_df)
st.write(second_candidate_df)
# st.write("Data grouped by candidate and state:")
# st.dataframe(df1)

# st.write("Data grouped by state and candidate:")
# st.dataframe(df2)
