#!/usr/bin/env python3
"""
Question 1: For each IP address, check how many requests came in after 
the first request in a 10-second window.
"""

import re
from datetime import datetime, timedelta
from collections import defaultdict

# Read the log file
with open('NodeJsApp.log', 'r') as file:
    log_lines = file.readlines()

# Dictionary to store IP addresses and their request timestamps
ip_requests = defaultdict(list)

# Regular expression to parse log entries
# Assumes common log format: IP - - [timestamp] "method endpoint" status size
log_pattern = r'^(\d+\.\d+\.\d+\.\d+).*?\[([^\]]+)\]'

# Parse each log line to extract IP and timestamp
for line in log_lines:
    match = re.match(log_pattern, line.strip())
    if match:
        ip_address = match.group(1)
        timestamp_str = match.group(2)
        
        # Parse timestamp (adjust format as needed for your log)
        # Common format: "10/Oct/2000:13:55:36 +0000"
        try:
            # Remove timezone info for simplicity
            timestamp_clean = timestamp_str.split(' ')[0]
            timestamp = datetime.strptime(timestamp_clean, '%d/%b/%Y:%H:%M:%S')
            ip_requests[ip_address].append(timestamp)
        except ValueError:
            # Skip lines with unparseable timestamps
            continue

# Analyze requests within 10-second windows for each IP
results = {}

for ip, timestamps in ip_requests.items():
    # Sort timestamps to process chronologically
    timestamps.sort()
    
    if len(timestamps) < 2:
        # Need at least 2 requests to have "requests after first"
        results[ip] = 0
        continue
    
    # Count requests in 10-second window after first request
    first_request = timestamps[0]
    window_end = first_request + timedelta(seconds=10)
    
    # Count requests after first request within the 10-second window
    requests_in_window = 0
    for timestamp in timestamps[1:]:  # Skip first request
        if timestamp <= window_end:
            requests_in_window += 1
        else:
            break  # Timestamps are sorted, so we can break early
    
    results[ip] = requests_in_window

# Write results to output file
with open('ip_request_analysis.txt', 'w') as output_file:
    output_file.write("IP Address Request Analysis - 10 Second Window\n")
    output_file.write("=" * 50 + "\n\n")
    
    # Sort by IP address for consistent output
    for ip in sorted(results.keys()):
        count = results[ip]
        output_file.write(f"{ip}: {count} requests after first request in 10-second window\n")

print("Analysis complete. Results saved to 'ip_request_analysis.txt'")