"""Task 9: Exporting Data"""
import os
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))

# Process the dataset
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
df["Payment_Mode"] = df["Payment_Mode"].fillna(df["Payment_Mode"].mode()[0])
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Discount"] = df["Discount"].fillna(0)
df["Rating"] = df["Rating"].fillna(round(df["Rating"].mean(), 1))
df["Revenue"] = (df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])).round(2)
print("Processed DataFrame shape:", df.shape)
print("Missing values remaining:", df.isnull().sum().sum())

# Export
out_path = os.path.join(BASE, "output", "cleaned_sales_data.csv")
df.to_csv(out_path, index=False)
print("\nExported to:", os.path.relpath(out_path, BASE))

# Verify
check = pd.read_csv(out_path)
print("\n--- Verification ---")
print("File exists:", os.path.exists(out_path))
print("File size (KB):", round(os.path.getsize(out_path) / 1024, 1))
print("Re-read shape:", check.shape)
print("Same shape as processed data:", check.shape == df.shape)
print("Columns:", list(check.columns))
print("Missing values in exported file:", check.isnull().sum().sum())
print(check.head())
