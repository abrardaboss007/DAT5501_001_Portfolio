import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "US-2016-primary.csv")
df = pd.read_csv(csv_path, sep = ";")


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
        else:
            first_candidate_option = st.selectbox(label="Select candidate", options=candidates_list, index=None, placeholder="Click to select...")

with col3:
    if compare_candidates_option:
        with st.container(border=True):
            second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
            second_candidate_option = st.selectbox(label="Select second candidate", options=second_candidate_options, index=None, placeholder="Click to select...")

#incorporate option that removes the option that user selected first
df1  = df.groupby(["candidate","state"])

df2 = df.groupby(["state","candidate"])

st.write(df1)
st.write(df2)