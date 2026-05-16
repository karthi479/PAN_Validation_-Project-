import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# Load Dataset
# --------------------------------
df = pd.read_csv(
    "cleaned_pan_dataset.csv"
)

# --------------------------------
# Dashboard Title
# --------------------------------
st.title(
    "PAN Validation Dashboard"
)

# --------------------------------
# Metrics
# --------------------------------
total_records = len(df)

valid_count = len(
    df[df["Status"] == True]
)

invalid_count = len(
    df[df["Status"] == False]
)

duplicate_count = df[
    "Duplicate"
].sum()

# --------------------------------
# Show Metrics
# --------------------------------
st.metric(
    "Total Records",
    total_records
)

st.metric(
    "Valid PANs",
    valid_count
)

st.metric(
    "Invalid PANs",
    invalid_count
)

st.metric(
    "Duplicate PANs",
    duplicate_count
)

# --------------------------------
# Display Dataset
# --------------------------------
st.subheader(
    "Dataset Preview"
)

st.dataframe(df)

# --------------------------------
# Chart
# --------------------------------
st.subheader(
    "PAN Status Chart"
)

status_counts = df[
    "Status"
].value_counts()

fig, ax = plt.subplots()

status_counts.plot(
    kind="bar",
    ax=ax
)

plt.title(
    "Valid vs Invalid PANs"
)

plt.xlabel(
    "Status"
)

plt.ylabel(
    "Count"
)

st.pyplot(fig)