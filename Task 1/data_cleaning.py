import pandas as pd
import os

print("Starting Data Cleaning Process...\n")

# dataset file name
file_name = "ecommerce_data.csv"

# check if dataset exists
if not os.path.exists(file_name):
    print("ERROR: Dataset file not found!")
    print("Make sure the file is in the same folder as this script.")
    exit()

# load dataset
print("Loading dataset...")
df = pd.read_csv(file_name, encoding="latin1")

# show first rows
print("\nFirst 5 rows:")
print(df.head())

# dataset info
print("\nDataset Info:")
print(df.info())

# missing values
print("\nMissing Values:")
print(df.isnull().sum())

# duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# remove missing customer id
print("\nRemoving rows with missing CustomerID...")
df = df.dropna(subset=["CustomerID"])

# remove duplicates
print("Removing duplicate rows...")
df = df.drop_duplicates()

# remove cancelled invoices (InvoiceNo starting with C)
print("Removing cancelled orders...")
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# convert date safely
print("Converting InvoiceDate to datetime...")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# remove invalid dates
df = df.dropna(subset=["InvoiceDate"])

# create TotalPrice column
print("Creating TotalPrice column...")
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# extract month and year
print("Extracting Month and Year...")
df["Month"] = df["InvoiceDate"].dt.month
df["Year"] = df["InvoiceDate"].dt.year

# remove negative quantities
print("Removing negative quantities...")
df = df[df["Quantity"] > 0]

# save cleaned dataset
clean_file = "cleaned_ecommerce_data.csv"
df.to_csv(clean_file, index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as:", clean_file)