import pandas as pd
import re

def clean_amount(value):
    value = re.sub(r"[^\d]", "", str(value))
    return int(value)

def transform(customers_df, orders_df):
    orders_df["amount"] = orders_df["amount"].apply(clean_amount)
    orders_df["order_date"] = pd.to_datetime(
        orders_df["order_date"], errors="coerce"
    )

    merged_df = orders_df.merge(customers_df, on="customer_id", how="left")

    return merged_df