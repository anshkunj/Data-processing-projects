# Data Validation & Quality Checks (Python)

## 📌 Overview
This project validates raw CSV data using rule-based checks before it is used for
analytics or reporting.

## 🧩 Validation Rules
- Mandatory fields must not be empty
- Email must follow a valid format
- Price must be a positive number
- Order date must be valid

## 🛠️ Tools Used
- Python
- Pandas
- Regex

## ⚙️ Workflow
1. Load raw data
2. Apply validation rules row-by-row
3. Separate valid and invalid records
4. Generate validation report

## 📂 Files
- `data.csv` → raw input
- `validate.py` → validation logic
- `valid_data.csv` → clean data
- `invalid_data.csv` → rejected data
- `validation_report.txt` → summary
- `PROBLEM.md` → problem definition

## ✅ Result
Ensured data quality by validating and categorizing records with clear error reasons.