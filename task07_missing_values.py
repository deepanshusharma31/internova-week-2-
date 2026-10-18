"""Task 7: Handling Missing Values"""
import os
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))

print("=== BEFORE handling missing values ===")
print("Shape:", df.shape)
print("\nRows with at least one missing value (first 5):")
print(df[df.isnull().any(axis=1)].head())
print("\nMissing values per column (isnull().sum()):\n", df.isnull().sum())
print("Total missing cells:", df.isna().sum().sum())

# Option 1: drop rows
dropped = df.dropna()
print("\n=== Option 1: dropna() ===")
print("Shape after dropping:", dropped.shape,
      "| rows lost:", df.shape[0] - dropped.shape[0])

# Option 2: fill with suitable values
filled = df.copy()
filled["Region"] = filled["Region"].fillna(filled["Region"].mode()[0])
filled["Payment_Mode"] = filled["Payment_Mode"].fillna(filled["Payment_Mode"].mode()[0])
filled["Quantity"] = filled["Quantity"].fillna(filled["Quantity"].median())
filled["Discount"] = filled["Discount"].fillna(0)
filled["Rating"] = filled["Rating"].fillna(round(filled["Rating"].mean(), 1))

print("\n=== Option 2: fillna() ===")
print("Region/Payment_Mode -> mode | Quantity -> median | Discount -> 0 | Rating -> mean")
print("\nMissing values per column AFTER filling:\n", filled.isnull().sum())
print("Shape after filling:", filled.shape)
print("\nSample of the filled dataset:\n", filled.head())

print("""
Why handling missing data matters in Data Analytics:
 - Missing values bias averages, totals and trends, giving wrong conclusions.
 - Many functions and ML models fail or silently skip rows containing NaN.
 - Dropping too many rows wastes data; filling carelessly adds false information,
   so the method must suit the column (mode for categories, median for skewed numbers).
 - Clean data makes results reliable and reproducible.""")
