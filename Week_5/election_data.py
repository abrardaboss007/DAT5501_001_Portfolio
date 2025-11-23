# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import streamlit as st
# import os

# # Load data
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# csv_path = os.path.join(BASE_DIR, "US-2016-primary.csv")
# df = pd.read_csv(csv_path, sep = ";")

# candidates_list = df["candidate"].unique().tolist()
# df["votes"] = pd.to_numeric(df["votes"],errors="coerce")
# df["fraction_votes"] = pd.to_numeric(df["fraction_votes"],errors="coerce")

# compare_candidates_option = st.toggle(label="Compare the vote fraction for two candidates", value=False)
# col1, col2 = st.columns(2)

# with col1:
#     with st.container(border=True):
#         if compare_candidates_option:
#             first_candidate_option = st.selectbox(label="Select first candidate", options=candidates_list, index=None, placeholder="Click to select...")
#             try:
#                 first_candidate_df = df[df["candidate"] == first_candidate_option]
#             except Exception as e:
#                 st.warning("Hey Ed! Please select first candidate above please!")
#             with col2:
#                 with st.container(border=True):
#                     second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
#                     second_candidate_option = st.selectbox(label="Select second candidate", options=second_candidate_options, index=None, placeholder="Click to select...")
#                     try:
#                         second_candidate_df = df[df["candidate"] == second_candidate_option]
#                     except Exception as e:
#                         st.warning("Hey Ed! Please select second candidate above please!")
#         else:
#             first_candidate_option = st.selectbox(label="Select candidate", options=candidates_list, index=None, placeholder="Click to select...")
#             try:
#                 first_candidate_df = df[df["candidate"] == first_candidate_option]
#             except Exception as e:
#                 st.warning("Hey Ed! Please select candidate name above please!")
# first_candidate_df = first_candidate_df.groupby(["state"])[["votes", "fraction_votes"]].sum()
# second_candidate_df = second_candidate_df.groupby(["state"])[["votes", "fraction_votes"]].sum()
# st.write(df)
# st.write(first_candidate_df)
# st.write(second_candidate_df)
# # st.write("Data grouped by candidate and state:")
# # st.dataframe(df1)

# # st.write("Data grouped by state and candidate:")
# # st.dataframe(df2)

# Ensure numeric
# df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
# df["fraction_votes"] = pd.to_numeric(df["fraction_votes"], errors="coerce")

# candidates_list = df["candidate"].unique().tolist()

# st.title("US 2016 Primary Election Vote Fraction Visualization")

# # Layout columns for selection
# col1, col2, col3 = st.columns(3)

# with col1:
#     compare_candidates_option = st.toggle(label="Compare vote fraction for two candidates", value=False)

# if not compare_candidates_option:
#     with col2:
#         # Select one candidate
#         first_candidate_option = st.selectbox("Select candidate", options=candidates_list, index=0)
    
#     if first_candidate_option:
#         # Filter data for candidate
#         candidate_df = df[df["candidate"] == first_candidate_option]

#         st.write(f"### Histogram of fraction of votes for {first_candidate_option} by state")

#         fig, ax = plt.subplots(figsize=(10, 5))
#         sns.histplot(candidate_df["fraction_votes"].dropna(), bins=20, kde=True, ax=ax)
#         ax.set_xlabel("Fraction of Votes")
#         ax.set_ylabel("Number of States")
#         ax.set_title(f"Vote Fraction Distribution for {first_candidate_option}")
#         st.pyplot(fig)

# else:
#     with col2:
#         # First candidate select box
#         first_candidate_option = st.selectbox("Select first candidate", options=candidates_list, index=0)
#     with col3:
#         # Exclude first candidate from second candidate options
#         second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
#         second_candidate_option = st.selectbox("Select second candidate", options=second_candidate_options, index=0)

#     if first_candidate_option and second_candidate_option:
#         first_df = df[df["candidate"] == first_candidate_option]
#         second_df = df[df["candidate"] == second_candidate_option]

#         st.write(f"### Comparing vote fractions between {first_candidate_option} and {second_candidate_option}")

#         fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)

#         sns.histplot(first_df["fraction_votes"].dropna(), bins=20, kde=True, ax=axes[0], color="blue")
#         axes[0].set_title(first_candidate_option)
#         axes[0].set_xlabel("Fraction of Votes")
#         axes[0].set_ylabel("Number of States")

#         sns.histplot(second_df["fraction_votes"].dropna(), bins=20, kde=True, ax=axes[1], color="orange")
#         axes[1].set_title(second_candidate_option)
#         axes[1].set_xlabel("Fraction of Votes")
#         # y-label is shared

#         st.pyplot(fig)


# # Read CSV; your data uses semicolon separator
# df = pd.read_csv(csv_path, sep=";")

# # Ensure numeric
# df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
# df["fraction_votes"] = pd.to_numeric(df["fraction_votes"], errors="coerce")

# candidates_list = df["candidate"].unique().tolist()

# st.title("US 2016 Primary Election: Vote Fraction by State")

# compare_candidates_option = st.toggle(
#     label="Compare vote fraction for two candidates",
#     value=False
# )

# if not compare_candidates_option:
#     candidate = st.selectbox("Select candidate", options=candidates_list, index=0)
    
#     # Aggregate: mean fraction_votes by state for candidate
#     candidate_df = df[df["candidate"] == candidate]
    
#     # Group by state: mean fraction_votes
#     state_agg = candidate_df.groupby("state")["fraction_votes"].mean().dropna()
    
#     st.write(f"### Distribution of mean fraction votes for '{candidate}' by state")
    
#     fig, ax = plt.subplots(figsize=(10, 5))
#     sns.histplot(state_agg, bins=20, kde=True, ax=ax)
#     ax.set_xlabel("Mean Fraction of Votes by State")
#     ax.set_ylabel("Number of States")
#     ax.set_title(f"Histogram of Mean Fraction Votes for {candidate}")
#     st.pyplot(fig)

# else:
#     col1, col2 = st.columns(2)
#     with col1:
#         first_candidate = st.selectbox("Select first candidate", options=candidates_list, index=0)
#     with col2:
#         candidates_ex_first = [c for c in candidates_list if c != first_candidate]
#         second_candidate = st.selectbox("Select second candidate", options=candidates_ex_first, index=0)
    
#     # Aggregate for first candidate
#     df1 = df[df["candidate"] == first_candidate]
#     agg1 = df1.groupby("state")["fraction_votes"].mean().dropna()
    
#     # Aggregate for second candidate
#     df2 = df[df["candidate"] == second_candidate]
#     agg2 = df2.groupby("state")["fraction_votes"].mean().dropna()
    
#     st.write(f"### Compare mean fraction votes: {first_candidate} vs {second_candidate}")
    
#     fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
    
#     sns.histplot(agg1, bins=20, kde=True, color="blue", ax=axes[0])
#     axes[0].set_title(first_candidate)
#     axes[0].set_xlabel("Mean Fraction Votes by State")
#     axes[0].set_ylabel("Number of States")
    
#     sns.histplot(agg2, bins=20, kde=True, color="orange", ax=axes[1])
#     axes[1].set_title(second_candidate)
#     axes[1].set_xlabel("Mean Fraction Votes by State")
#     # y label shared
    
#     st.pyplot(fig)

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

df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
df["fraction_votes"] = pd.to_numeric(df["fraction_votes"], errors="coerce")
candidates_list = df["candidate"].unique().tolist()

st.title("US 2016 Primary Election: Vote Fraction by State")

compare_candidates_option = st.toggle(
    label="Compare the vote fraction for two candidates",
    value=False
)

if compare_candidates_option:
    col1, col2 = st.columns(2)
    with col1:
        first_candidate_option = st.selectbox("Select first candidate", options=candidates_list)
    with col2:
        second_candidate_options = [c for c in candidates_list if c != first_candidate_option]
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

    fig, ax = plt.subplots(figsize=(15, 7))
    plot_df.plot(kind="bar", ax=ax)
    ax.set_ylabel("Fraction of Votes")
    ax.set_xlabel("State")
    ax.set_title("Vote Fraction by State")
    ax.legend(title="Candidate")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

else:
    candidate_option = st.selectbox("Select candidate", options=candidates_list)

    total_votes_by_state = df.groupby("state")["votes"].sum()
    candidate_votes = df[df["candidate"] == candidate_option].groupby("state")["votes"].sum()
    fraction = (candidate_votes / total_votes_by_state).dropna()

    st.subheader(f"Vote fraction by state: {candidate_option}")

    fig, ax = plt.subplots(figsize=(15, 7))
    fraction.plot(kind="bar", color="green", ax=ax)
    ax.set_ylabel("Fraction of Votes")
    ax.set_xlabel("State")
    ax.set_title(f"Vote Fraction by State for {candidate_option}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)