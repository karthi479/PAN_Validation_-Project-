# PAN Validation Project

## Overview

This project is a Python-based PAN Card Validation and Data Cleaning Pipeline developed using Pandas, Regex, Matplotlib, and Streamlit.

The system validates PAN numbers, detects duplicates, handles null values, cleans messy datasets, generates reports, exports CSV files, and visualizes analytics through a dashboard.

---

## Features

- PAN Card Validation
- Data Cleaning
- Duplicate Detection
- Null Value Handling
- CSV Export
- Summary Reporting
- Data Visualization
- Streamlit Dashboard

---

## Tech Stack

- Python
- Pandas
- Regex
- Matplotlib
- Streamlit

---

## Project Structure

```text
PAN_Validation_Project/
│
├── project.py
├── dashboard.py
├── cleaned_pan_dataset.csv
├── valid_pans.csv
├── invalid_pans.csv
├── duplicate_pans.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Install required libraries:

```bash
pip install pandas matplotlib streamlit
```

---

## Run Project

Run main pipeline:

```bash
python project.py
```

Run dashboard:

```bash
streamlit run dashboard.py
```

---

## Output

The project generates:

- Cleaned PAN dataset
- Valid PAN report
- Invalid PAN report
- Duplicate PAN report
- Summary analytics
- Dashboard visualization

---

## Dashboard Preview

Add screenshot here later.

---

## Future Improvements

- SQL Integration
- Flask API
- Login Authentication
- Cloud Deployment
- Real-time PAN Validation
