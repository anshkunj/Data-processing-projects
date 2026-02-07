from collections import defaultdict
import re

ip_count = defaultdict(int)
endpoint_count = defaultdict(int)
error_count = 0

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+).+"(?P<method>GET|POST|PUT|DELETE)\s(?P<endpoint>/\S+).+"\s(?P<status>\d{3})'
)

with open("server.log", "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if not match:
            continue

        ip = match.group("ip")
        endpoint = match.group("endpoint")
        status = int(match.group("status"))

        ip_count[ip] += 1
        endpoint_count[endpoint] += 1

        if status >= 400:
            error_count += 1

print("📊 Log Analysis Report")
print("-" * 30)

print("\nTop IPs:")
for ip, count in sorted(ip_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip}: {count} requests")

print("\nTop Endpoints:")
for ep, count in sorted(endpoint_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{ep}: {count} hits")

print(f"\n❌ Total Errors (4xx & 5xx): {error_count}")
