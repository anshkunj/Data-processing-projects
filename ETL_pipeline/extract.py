import pandas as pd
import json

def extract_customers(path):
    return pd.read_csv(path)

def extract_orders(path):
    with open(path, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)