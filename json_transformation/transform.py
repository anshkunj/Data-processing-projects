import json
import pandas as pd
import re

def clean_amount(value):
    value = re.sub(r"[^\d]", "", value)
    return int(value)

# Load JSON
with open("input.json", "r") as f:
    data = json.load(f)

records = []

for item in data:
    record = {
        "user_id": item["user"]["id"],
        "user_name": item["user"]["name"],
        "user_email": item["user"]["email"],
        "order_id": item["order"]["order_id"],
        "order_amount": clean_amount(item["order"]["amount"]),
        "order_date": pd.to_datetime(item["order"]["date"], errors="coerce")
    }
    records.append(record)

df = pd.DataFrame(records)

# Standardize date format
df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

# Save output
df.to_csv("output.csv", index=False)

print("✅ JSON transformed into CSV successfully.")