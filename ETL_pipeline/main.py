from extract import extract_customers, extract_orders
from transform import transform
from load import load_to_db

customers = extract_customers("data/customers.csv")
orders = extract_orders("data/orders.json")

final_df = transform(customers, orders)

load_to_db(final_df)

print("✅ ETL pipeline executed successfully.")