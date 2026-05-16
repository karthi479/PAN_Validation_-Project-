import pandas as pd
import random
import string
import re
import matplotlib.pyplot as plt

# --------------------------------
# Generate Valid PAN
# --------------------------------
def generate_valid_pan():

    letters = ''.join(
        random.choices(string.ascii_uppercase, k=5)
    )

    digits = ''.join(
        random.choices(string.digits, k=4)
    )

    last_letter = random.choice(
        string.ascii_uppercase
    )

    return letters + digits + last_letter


# --------------------------------
# Generate Invalid PAN
# --------------------------------
def generate_invalid_pan():

    invalid_list = [
        "12345ABCDE",
        "ABCDE12345",
        "AB12E1234F",
        "abcde1234f",
        "ABCDE12F4F",
        "AB@DE1234F",
        " ABCDE1234F "
    ]

    return random.choice(invalid_list)


# --------------------------------
# Clean PAN
# --------------------------------
def clean_pan(pan):

    if pd.isna(pan):
        return None

    pan = str(pan).strip()

    pan = pan.upper()

    return pan


# --------------------------------
# Validate PAN
# --------------------------------
def validate_pan(pan):

    # Handle null values
    if pd.isna(pan):
        return False

    pan = str(pan)

    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

    return bool(
        re.match(pattern, pan)
    )


# --------------------------------
# Create Dataset
# --------------------------------
data = []

for i in range(20):

    if random.random() < 0.7:
        pan = generate_valid_pan()
    else:
        pan = generate_invalid_pan()

    data.append({
        "Customer_ID": i + 1,
        "PAN_Number": pan
    })

# --------------------------------
# Create DataFrame
# --------------------------------
df = pd.DataFrame(data)

# --------------------------------
# Add Duplicate
# --------------------------------
df.loc[5, "PAN_Number"] = df.loc[2, "PAN_Number"]

# --------------------------------
# Add Null Value
# --------------------------------
df.loc[8, "PAN_Number"] = None

# --------------------------------
# Clean PANs
# --------------------------------
df["Cleaned_PAN"] = df[
    "PAN_Number"
].apply(clean_pan)

# --------------------------------
# Validate PANs
# --------------------------------
df["Status"] = df[
    "Cleaned_PAN"
].apply(validate_pan)

# --------------------------------
# Detect Duplicates
# --------------------------------
df["Duplicate"] = df[
    "Cleaned_PAN"
].duplicated(keep=False)

# --------------------------------
# Save CSV
# --------------------------------
df.to_csv(
    "cleaned_pan_dataset.csv",
    index=False
)

# --------------------------------
# Print Output
# --------------------------------
print(df)

print("\nCleaned Dataset Created Successfully")

# --------------------------------
# Separate Valid PANs
# --------------------------------
valid_df = df[
    df["Status"] == True
]

# Save Valid PANs
valid_df.to_csv(
    "valid_pans.csv",
    index=False
)

# --------------------------------
# Separate Invalid PANs
# --------------------------------
invalid_df = df[
    df["Status"] == False
]

# Save Invalid PANs
invalid_df.to_csv(
    "invalid_pans.csv",
    index=False
)

print("\nValid and Invalid PAN files created")

# --------------------------------
# Summary Report
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

null_count = df[
    "PAN_Number"
].isna().sum()

# --------------------------------
# Print Summary
# --------------------------------
print("\n----- SUMMARY REPORT -----")

print(f"Total Records : {total_records}")

print(f"Valid PANs    : {valid_count}")

print(f"Invalid PANs  : {invalid_count}")

print(f"Duplicate PANs: {duplicate_count}")

print(f"Null Values   : {null_count}")

# --------------------------------
# Visualization
# --------------------------------

status_counts = df["Status"].value_counts()

# Create Bar Chart
status_counts.plot(
    kind="bar"
)

# Chart Title
plt.title(
    "Valid vs Invalid PANs"
)

# X-axis Label
plt.xlabel(
    "PAN Status"
)

# Y-axis Label
plt.ylabel(
    "Count"
)

# Show Chart
plt.show()