import pandas as pd

# Load data
df = pd.read_csv("transactions.csv", parse_dates=["order_date"])

# -----------------------------
# 1. Total spend per customer
# -----------------------------
customer_spend = (
    df.groupby("customer_id")["price"]
    .sum()
    .reset_index()
    .rename(columns={"price": "total_spend"})
)

# -----------------------------
# 2. Monthly revenue trend
# -----------------------------
df["month"] = df["order_date"].dt.to_period("M")
monthly_revenue = (
    df.groupby("month")["price"]
    .sum()
    .reset_index()
)

# -----------------------------
# 3. Top products per category
# -----------------------------
top_products = (
    df.groupby(["category", "product"])["price"]
    .sum()
    .reset_index()
    .sort_values(["category", "price"], ascending=[True, False])
    .groupby("category")
    .head(1)
)

# -----------------------------
# 4. Inactive customers
# -----------------------------
last_date = df["order_date"].max()
inactive_customers = (
    df.groupby("customer_id")["order_date"]
    .max()
    .reset_index()
)

inactive_customers = inactive_customers[
    inactive_customers["order_date"] < (last_date - pd.Timedelta(days=60))
]

# -----------------------------
# Save outputs
# -----------------------------
customer_spend.to_csv("customer_spend.csv", index=False)
monthly_revenue.to_csv("monthly_revenue.csv", index=False)
top_products.to_csv("top_products.csv", index=False)
inactive_customers.to_csv("inactive_customers.csv", index=False)

print("✅ Customer analysis completed. Reports generated.")