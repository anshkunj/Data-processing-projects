import pandas as pd
import os

INPUT_DIR = "input_excels"
OUTPUT_FILE = "final_report.xlsx"

all_dfs = []

for file in os.listdir(INPUT_DIR):
    if file.endswith(".xlsx"):
        file_path = os.path.join(INPUT_DIR, file)
        df = pd.read_excel(file_path)

        # Standardize column names
        df.columns = [col.lower() for col in df.columns]
        df = df.rename(columns={"dept": "department"})

        all_dfs.append(df)

# Merge all files
merged_df = pd.concat(all_dfs, ignore_index=True)

# Department-wise summary
summary_df = (
    merged_df.groupby("department")["revenue"]
    .sum()
    .reset_index()
)

# Write to Excel with multiple sheets
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    merged_df.to_excel(writer, sheet_name="Merged_Data", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)

print("✅ Excel automation completed. Report generated.")