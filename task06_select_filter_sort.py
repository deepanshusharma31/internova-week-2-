"""Task 6: Selecting, Filtering & Sorting Data"""
import os
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))

print("--- Select specific columns ---")
print(df[["Order_ID", "Region", "Unit_Price"]].head())

print("\n--- Select specific rows ---")
print("Rows 5 to 9 using iloc:\n", df.iloc[5:10])
print("\nRows using loc (index 0, 2, 4), selected columns:\n",
      df.loc[[0, 2, 4], ["Order_ID", "Product_ID", "Quantity"]])

print("\n--- Filter on a condition (Unit_Price > 20000) ---")
expensive = df[df["Unit_Price"] > 20000]
print(expensive.head())
print("Matching rows:", len(expensive))

print("\n--- Multiple conditions (Region = North AND Quantity >= 5) ---")
multi = df[(df["Region"] == "North") & (df["Quantity"] >= 5)]
print(multi.head())
print("Matching rows:", len(multi))

print("\n--- Multiple conditions with OR (UPI or Cash, Rating >= 4) ---")
either = df[(df["Payment_Mode"].isin(["UPI", "Cash"])) & (df["Rating"] >= 4)]
print(either.head())
print("Matching rows:", len(either))

print("\n--- Sort ascending by Unit_Price ---")
print(df.sort_values("Unit_Price", ascending=True)[
    ["Order_ID", "Product_ID", "Unit_Price"]].head())

print("\n--- Sort descending by Unit_Price, then Quantity ---")
print(df.sort_values(["Unit_Price", "Quantity"], ascending=[False, False])[
    ["Order_ID", "Product_ID", "Unit_Price", "Quantity"]].head())
