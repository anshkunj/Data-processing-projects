# Problem Statement

A system receives real-time sensor data where each record contains a timestamp
and a numeric value (e.g., temperature, CPU usage, traffic count).

The data arrives continuously and must be processed in near real-time.

### Challenges:
- Data is streamed, not batch
- Cannot wait for full dataset
- Need rolling statistics
- Need anomaly detection

### Objectives:
- Simulate a real-time data stream
- Compute rolling average
- Detect anomalies based on threshold
- Store processed output

### Expected Output:
- Streamed data processing
- Rolling average values
- Anomaly alerts
- Processed output file