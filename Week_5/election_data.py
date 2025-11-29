# Hey Ed, in order to run this file as well as all others please navigate to the main.py file, open a new terminal and write streamlit run main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# Load data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "US-2016-primary.csv")
df = pd.read_csv(csv_path, sep=";")

# Convert votes and fraction votes columns to numerica data type
df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
df["fraction_votes"] = pd.to_numeric(df["fraction_votes"], errors="coerce")

# Get list of all candidates
candidates_list = df["candidate"].unique().tolist()

st.title("US 2016 Primary Election: Vote Fraction by State")

# Allow user to compare vote fraction for two candidates
compare_candidates_option = st.toggle(label="Compare the vote fraction for two candidates", 
                                      value=False)

if compare_candidates_option:
    col1, col2 = st.columns(2)
    with col1:
        first_candidate_option = st.selectbox("Select first candidate", options=candidates_list)
    with col2:
        second_candidate_options = [c for c in candidates_list if c != first_candidate_option] # Remove first candidate selected from list of second candidate options
        second_candidate_option = st.selectbox("Select second candidate", options=second_candidate_options)

    # Aggregate votes for denominator: total votes per state
    total_votes_by_state = df.groupby("state")["votes"].sum()

    # Aggregate votes for first candidate
    first_candidate_votes = df[df["candidate"] == first_candidate_option].groupby("state")["votes"].sum()
    first_fraction = (first_candidate_votes / total_votes_by_state).dropna()

    # Aggregate votes for second candidate
    second_candidate_votes = df[df["candidate"] == second_candidate_option].groupby("state")["votes"].sum()
    second_fraction = (second_candidate_votes / total_votes_by_state).dropna()

    # Get the union of states for both candidates
    all_states = sorted(set(first_fraction.index).union(second_fraction.index))

    # Create DataFrame for plotting
    plot_df = pd.DataFrame({
        first_candidate_option: first_fraction.reindex(all_states, fill_value=0),
        second_candidate_option: second_fraction.reindex(all_states, fill_value=0)
    }, index=all_states)

    st.subheader(f"Vote fraction by state: {first_candidate_option} vs {second_candidate_option}")

    # Display graph if user selects two candidates to compare
    fig, ax = plt.subplots(figsize=(15, 8))
    plot_df.plot(kind="bar", ax=ax)
    ax.set_ylabel("Fraction of Votes")
    ax.set_xlabel("State")
    ax.set_title("Vote Fraction by State")
    ax.legend(title="Candidate")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

else:
    # Display graph if user select only candidate to look at
    candidate_option = st.selectbox("Select candidate", options=candidates_list)

    total_votes_by_state = df.groupby("state")["votes"].sum()
    candidate_votes = df[df["candidate"] == candidate_option].groupby("state")["votes"].sum()
    fraction = (candidate_votes / total_votes_by_state).dropna()

    st.subheader(f"Vote fraction by state: {candidate_option}")

    fig, ax = plt.subplots(figsize=(15, 8))
    fraction.plot(kind="bar", color="green", ax=ax)
    ax.set_ylabel("Fraction of Votes")
    ax.set_xlabel("State")
    ax.set_title(f"Vote Fraction by State for {candidate_option}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)