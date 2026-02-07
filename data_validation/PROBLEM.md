# Problem Statement

A company receives datasets from multiple sources that may contain invalid or
inconsistent data. Before using this data for analytics or reporting, it must be
validated to ensure quality and correctness.

### Challenges:
- Presence of invalid values (negative prices, wrong emails, missing fields)
- Inconsistent date formats
- Mandatory columns may be missing or empty

### Objectives:
- Validate incoming data using predefined rules
- Separate valid and invalid records
- Generate a data quality report

### Validation Rules:
- Price must be a positive number
- Email must be in a valid format
- Order date must be a valid date
- Mandatory fields cannot be null

### Expected Output:
- Clean (valid) dataset
- Invalid records dataset
- Data validation summary report