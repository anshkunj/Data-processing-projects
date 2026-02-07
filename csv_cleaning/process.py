import pandas as pd
import re

def clean_price(price):
    if pd.isna(price):
        return None
    price = re.sub(r"[^\d]", "", str(price))
    return int(price) if price else None

# Load data
df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=["customer_name", "price"])

# Clean price column
df["price"] = df["price"].apply(clean_price)

# Convert date to standard format
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Drop rows with invalid dates
df = df.dropna(subset=["order_date"])

# Final formatting
df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("✅ Data cleaning completed. Output saved as cleaned_data.csv")
