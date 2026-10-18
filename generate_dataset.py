"""
generate_dataset.py
Creates the practice datasets used in all tasks (run once).
  data/sales_data.csv     - 600 orders, contains deliberate missing values
  data/products.csv       - product master (name, category, cost price)
  data/customers.csv      - customer master (segment)
"""
import os
import numpy as np
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(42)

# ---------- Products ----------
products = pd.DataFrame({
    "Product_ID": [f"P{str(i).zfill(2)}" for i in range(1, 13)],
    "Product_Name": ["Laptop", "Smartphone", "Headphones", "Smartwatch",
                     "Office Chair", "Study Desk", "LED Lamp", "Bookshelf",
                     "Notebook Pack", "Pen Set", "Backpack", "Water Bottle"],
    "Category": ["Electronics"] * 4 + ["Furniture"] * 4 + ["Stationery"] * 2
                + ["Accessories"] * 2,
    "Cost_Price": [42000, 15000, 1500, 4500, 4200, 5500, 450, 3200,
                   180, 90, 700, 250],
})
list_price = (products["Cost_Price"] * rng.uniform(1.2, 1.5, 12)).round(0)
price_map = dict(zip(products["Product_ID"], list_price))

# ---------- Customers ----------
customers = pd.DataFrame({
    "Customer_ID": [f"C{str(i).zfill(3)}" for i in range(1, 81)],
    "Segment": rng.choice(["Consumer", "Corporate", "Home Office"], 80,
                          p=[0.5, 0.3, 0.2]),
})

# ---------- Sales ----------
n = 600
pid = rng.choice(products["Product_ID"], n)
dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    rng.integers(0, 365, n), unit="D")
sales = pd.DataFrame({
    "Order_ID": [f"ORD{str(i).zfill(4)}" for i in range(1, n + 1)],
    "Order_Date": dates.strftime("%Y-%m-%d"),
    "Customer_ID": rng.choice(customers["Customer_ID"], n),
    "Product_ID": pid,
    "Region": rng.choice(["North", "South", "East", "West", "Central"], n),
    "Quantity": rng.integers(1, 8, n).astype(float),
    "Unit_Price": pd.Series(pid).map(price_map).values,
    "Discount": rng.choice([0.0, 0.05, 0.10, 0.15, 0.20], n,
                           p=[0.4, 0.2, 0.2, 0.1, 0.1]),
    "Payment_Mode": rng.choice(["UPI", "Credit Card", "Debit Card", "Cash",
                                "Net Banking"], n, p=[0.35, 0.25, 0.2, 0.1, 0.1]),
    "Rating": rng.integers(1, 6, n).astype(float),
})
sales = sales.sort_values("Order_Date").reset_index(drop=True)
sales["Order_ID"] = [f"ORD{str(i).zfill(4)}" for i in range(1, n + 1)]

# ---------- Inject missing values ----------
for col, frac in {"Region": 0.04, "Quantity": 0.03, "Discount": 0.06,
                  "Rating": 0.08, "Payment_Mode": 0.03}.items():
    idx = rng.choice(n, int(n * frac), replace=False)
    sales.loc[idx, col] = np.nan

sales.to_csv(os.path.join(BASE, "data", "sales_data.csv"), index=False)
products.to_csv(os.path.join(BASE, "data", "products.csv"), index=False)
customers.to_csv(os.path.join(BASE, "data", "customers.csv"), index=False)
print("Datasets created:", sales.shape, products.shape, customers.shape)
