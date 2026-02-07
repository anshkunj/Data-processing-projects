# Problem Statement

A company generates large server log files that are difficult to analyze manually.
The logs contain information about client IP addresses, HTTP requests, endpoints,
and response status codes.

### Challenges:
- Log files can be very large (GBs in size)
- Data is unstructured text
- Must be processed efficiently without loading the entire file into memory

### Objectives:
- Count total requests per IP address
- Identify most frequently accessed endpoints
- Calculate total error responses (4xx and 5xx)

### Constraints:
- Solution must be memory-efficient
- Processing should be done line by line
- Code should be scalable to large log files

### Expected Output:
- Summary report showing:
  - Top IP addresses by request count
  - Most accessed endpoints
  - Total number of error responses
