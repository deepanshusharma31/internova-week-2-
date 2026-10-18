"""Task 8: Merge, Concatenate, GroupBy & Pivot Table"""
import os
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))
sales = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))
products = pd.read_csv(os.path.join(BASE, "data", "products.csv"))
customers = pd.read_csv(os.path.join(BASE, "data", "customers.csv"))

# quick cleaning so aggregates are meaningful
sales["Region"] = sales["Region"].fillna("Unknown")
sales["Quantity"] = sales["Quantity"].fillna(sales["Quantity"].median())
sales["Discount"] = sales["Discount"].fillna(0)

print("=== MERGE ===")
merged = sales.merge(products, on="Product_ID", how="left")
merged = merged.merge(customers, on="Customer_ID", how="left")
merged["Revenue"] = (merged["Quantity"] * merged["Unit_Price"]
                     * (1 - merged["Discount"])).round(2)
print("Merged on Product_ID and Customer_ID. Shape:", merged.shape)
print(merged[["Order_ID", "Product_Name", "Category", "Segment", "Revenue"]].head())

print("\n=== CONCATENATE ===")
h1 = merged[merged["Order_Date"] < "2025-07-01"]
h2 = merged[merged["Order_Date"] >= "2025-07-01"]
print("First half rows:", len(h1), "| Second half rows:", len(h2))
combined = pd.concat([h1, h2], ignore_index=True)
print("After concat rows:", len(combined), "(equals original:", len(combined) == len(merged), ")")

print("\n=== GROUPBY ===")
print("Total revenue by Category:\n", merged.groupby("Category")["Revenue"].sum().round(2))
print("\nMultiple aggregates by Region:")
print(merged.groupby("Region")["Revenue"].agg(["sum", "mean", "count", "min", "max"]).round(2))
print("\nAverage Rating by Category:\n",
      merged.groupby("Category")["Rating"].mean().round(2))

print("\n=== PIVOT TABLE ===")
pivot = pd.pivot_table(merged, values="Revenue", index="Category",
                       columns="Region", aggfunc="sum", margins=True,
                       margins_name="Total", fill_value=0).round(0)
print("Revenue: Category (rows) x Region (columns)\n", pivot)

pivot2 = pd.pivot_table(merged, values="Quantity", index="Segment",
                        columns="Payment_Mode", aggfunc="sum", fill_value=0)
print("\nUnits sold: Segment x Payment_Mode\n", pivot2)
