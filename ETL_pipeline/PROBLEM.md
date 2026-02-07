# Problem Statement

A company receives data from multiple sources in different formats such as CSV and JSON.
This raw data cannot be used directly for analytics or reporting.

### Challenges:
- Multiple input formats (CSV + JSON)
- Inconsistent schemas
- Need a single clean storage layer

### Objectives:
- Extract data from CSV and JSON sources
- Transform and standardize the data
- Load the processed data into a database (SQLite)

### Expected Output:
- A SQLite database containing cleaned and merged data
- Modular ETL scripts (extract, transform, load)