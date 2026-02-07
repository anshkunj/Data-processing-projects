import time
import random
from datetime import datetime

def stream_data():
    while True:
        data_point = {
            "timestamp": datetime.now().isoformat(),
            "value": random.randint(20, 100)
        }
        yield data_point
        time.sleep(1)