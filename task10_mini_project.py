"""
Task 10: Mini Data Analysis Project - Sales Performance Analysis (2025)
Uses NumPy and Pandas on a sales dataset with product and customer tables.
"""
import os
import numpy as np
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)
BASE = os.path.dirname(os.path.abspath(__file__))

# 1. LOAD
print("=" * 70, "\n1. LOADING DATA\n", "=" * 70, sep="")
sales = pd.read_csv(os.path.join(BASE, "data", "sales_data.csv"))
products = pd.read_csv(os.path.join(BASE, "data", "products.csv"))
customers = pd.read_csv(os.path.join(BASE, "data", "customers.csv"))
print("Sales:", sales.shape, "| Products:", products.shape, "| Customers:", customers.shape)

# 2. INSPECT
print("\n" + "=" * 70, "\n2. DATA INSPECTION\n", "=" * 70, sep="")
print(sales.head())
print("\nData types:\n", sales.dtypes)
print("\nSummary statistics:\n", sales.describe().round(2))
print("\nDuplicate rows:", sales.duplicated().sum())

# 3. MISSING VALUES
print("\n" + "=" * 70, "\n3. MISSING VALUES\n", "=" * 70, sep="")
print("Missing before:\n", sales.isnull().sum())
sales["Region"] = sales["Region"].fillna(sales["Region"].mode()[0])
sales["Payment_Mode"] = sales["Payment_Mode"].fillna(sales["Payment_Mode"].mode()[0])
sales["Quantity"] = sales["Quantity"].fillna(sales["Quantity"].median())
sales["Discount"] = sales["Discount"].fillna(0)
sales["Rating"] = sales["Rating"].fillna(round(sales["Rating"].mean(), 1))
print("\nTotal missing after cleaning:", sales.isnull().sum().sum())

# Feature engineering (NumPy + Pandas)
df = sales.merge(products, on="Product_ID", how="left").merge(
    customers, on="Customer_ID", how="left")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month_name()
df["Month_Num"] = df["Order_Date"].dt.month
df["Revenue"] = np.round(df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"]), 2)
df["Profit"] = np.round(df["Revenue"] - df["Quantity"] * df["Cost_Price"], 2)
high_cut = np.percentile(df["Revenue"], 75)
df["Order_Value_Tier"] = np.where(df["Revenue"] >= high_cut, "High", "Regular")
print("\n75th percentile revenue (High-tier cutoff):", round(high_cut, 2))
print(df[["Order_ID", "Product_Name", "Revenue", "Profit", "Order_Value_Tier"]].head())

# 4. SELECT & FILTER
print("\n" + "=" * 70, "\n4. SELECTING & FILTERING\n", "=" * 70, sep="")
high_orders = df[df["Order_Value_Tier"] == "High"]
print("High-value orders:", len(high_orders))
elec_north = df[(df["Category"] == "Electronics") & (df["Region"] == "North")]
print("Electronics orders in North:", len(elec_north))
print(elec_north[["Order_ID", "Product_Name", "Quantity", "Revenue"]].head())

# 5. SORT
print("\n" + "=" * 70, "\n5. SORTING\n", "=" * 70, sep="")
print("Top 5 orders by revenue:")
print(df.sort_values("Revenue", ascending=False)[
    ["Order_ID", "Product_Name", "Region", "Revenue"]].head())

# 6. GROUPBY
print("\n" + "=" * 70, "\n6. GROUPBY ANALYSIS\n", "=" * 70, sep="")
by_cat = df.groupby("Category").agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum"),
                                    Orders=("Order_ID", "count"),
                                    Avg_Rating=("Rating", "mean")).round(2)
by_cat = by_cat.sort_values("Revenue", ascending=False)
print(by_cat)
by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).round(2)
print("\nRevenue by Region:\n", by_region)
by_prod = df.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).round(2)
print("\nTop 5 products by revenue:\n", by_prod.head())
by_pay = df["Payment_Mode"].value_counts(normalize=True).mul(100).round(1)
print("\nPayment mode share (%):\n", by_pay)
by_seg = df.groupby("Segment")["Revenue"].sum().sort_values(ascending=False).round(2)
print("\nRevenue by Segment:\n", by_seg)
by_month = df.groupby(["Month_Num", "Month"])["Revenue"].sum().round(2)
print("\nMonthly revenue:\n", by_month)

# 7. PIVOT TABLE
print("\n" + "=" * 70, "\n7. PIVOT TABLES\n", "=" * 70, sep="")
pv = pd.pivot_table(df, values="Revenue", index="Category", columns="Region",
                    aggfunc="sum", margins=True, margins_name="Total").round(0)
print("Revenue by Category x Region:\n", pv)
pv2 = pd.pivot_table(df, values="Profit", index="Segment", columns="Category",
                     aggfunc="mean").round(0)
print("\nAverage profit per order, Segment x Category:\n", pv2)

# 8. INSIGHTS
print("\n" + "=" * 70, "\n8. KEY INSIGHTS\n", "=" * 70, sep="")
total_rev, total_profit = df["Revenue"].sum(), df["Profit"].sum()
best_month = by_month.idxmax()[1]
worst_month = by_month.idxmin()[1]
disc_qty = df.groupby(df["Discount"] > 0)["Quantity"].mean().round(2)
margin = (df.groupby("Category")["Profit"].sum() / df.groupby("Category")["Revenue"].sum()
          * 100).round(1).sort_values(ascending=False)
print(f"1. Total revenue is Rs {total_rev:,.0f} with total profit Rs {total_profit:,.0f} "
      f"(overall margin {total_profit / total_rev * 100:.1f}%).")
print(f"2. {by_cat.index[0]} is the top category, contributing "
      f"{by_cat['Revenue'].iloc[0] / total_rev * 100:.1f}% of revenue.")
print(f"3. {by_region.index[0]} is the best region (Rs {by_region.iloc[0]:,.0f}); "
      f"{by_region.index[-1]} is the weakest (Rs {by_region.iloc[-1]:,.0f}).")
print(f"4. {by_prod.index[0]} is the best-selling product by revenue; "
      f"top 3 products give {by_prod.head(3).sum() / total_rev * 100:.1f}% of revenue.")
print(f"5. {best_month} has the highest monthly revenue and {worst_month} the lowest.")
print(f"6. {by_pay.index[0]} is the most used payment mode ({by_pay.iloc[0]}% of orders).")
print(f"7. Category with best profit margin: {margin.index[0]} ({margin.iloc[0]}%); "
      f"lowest: {margin.index[-1]} ({margin.iloc[-1]}%).")
print(f"8. Average units per order: discounted {disc_qty[True]} vs "
      f"non-discounted {disc_qty[False]}.")
print(f"9. {by_seg.index[0]} customers generate the most revenue "
      f"({by_seg.iloc[0] / total_rev * 100:.1f}%).")

# 9. EXPORT
print("\n" + "=" * 70, "\n9. EXPORT\n", "=" * 70, sep="")
out = os.path.join(BASE, "output", "project_cleaned_sales_analysis.csv")
df.drop(columns=["Month_Num"]).to_csv(out, index=False)
print("Saved:", os.path.relpath(out, BASE), "| shape:", pd.read_csv(out).shape)
