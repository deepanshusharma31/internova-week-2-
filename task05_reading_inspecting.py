"""Task 5: Reading & Inspecting Data"""
import os
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))

print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nNumber of rows and columns:", df.shape)
print("Rows:", df.shape[0], "| Columns:", df.shape[1])
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\ninfo():")
df.info()
print("\ndescribe():\n", df.describe())
