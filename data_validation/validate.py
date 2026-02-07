import pandas as pd
import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

df = pd.read_csv("data.csv")

valid_rows = []
invalid_rows = []

for _, row in df.iterrows():
    errors = []

    if pd.isna(row["customer_name"]):
        errors.append("Missing customer_name")

    if not re.match(EMAIL_REGEX, str(row["email"])):
        errors.append("Invalid email")

    if row["price"] <= 0:
        errors.append("Invalid price")

    try:
        pd.to_datetime(row["order_date"])
    except:
        errors.append("Invalid order_date")

    if errors:
        row["errors"] = "; ".join(errors)
        invalid_rows.append(row)
    else:
        valid_rows.append(row)

valid_df = pd.DataFrame(valid_rows)
invalid_df = pd.DataFrame(invalid_rows)

valid_df.to_csv("valid_data.csv", index=False)
invalid_df.to_csv("invalid_data.csv", index=False)

# Summary report
with open("validation_report.txt", "w") as f:
    f.write("Data Validation Report\n")
    f.write("======================\n")
    f.write(f"Total records: {len(df)}\n")
    f.write(f"Valid records: {len(valid_df)}\n")
    f.write(f"Invalid records: {len(invalid_df)}\n")

print("✅ Data validation completed. Reports generated.")