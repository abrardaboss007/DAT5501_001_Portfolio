# Import relevant modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st
#----------------------------------------------------------------------------------------------
# Change directory to mosque_finder folder
cwd = os.getcwd()
extra_part = "mosque_finder"
new_dir = os.path.join(cwd, extra_part)
os.chdir(new_dir)
#----------------------------------------------------------------------------------------------
# Display csv file
df = pd.read_csv("uk_mosques.csv", encoding="latin1", on_bad_lines="skip")

st.write(df)