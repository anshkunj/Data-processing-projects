from collections import deque
from stream_simulator import stream_data

WINDOW_SIZE = 5
ANOMALY_THRESHOLD = 90

window = deque(maxlen=WINDOW_SIZE)

with open("processed_stream.csv", "w") as f:
    f.write("timestamp,value,rolling_avg,anomaly\n")

    for data in stream_data():
        value = data["value"]
        window.append(value)

        rolling_avg = sum(window) / len(window)

        anomaly = "YES" if value >= ANOMALY_THRESHOLD else "NO"

        f.write(
            f"{data['timestamp']},{value},{rolling_avg:.2f},{anomaly}\n"
        )
        f.flush()

        print(
            f"Value: {value} | "
            f"Rolling Avg: {rolling_avg:.2f} | "
            f"Anomaly: {anomaly}"
        )