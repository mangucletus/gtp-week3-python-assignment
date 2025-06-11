#!/usr/bin/env python3
"""
Question 1: For each IP address, check how many requests came in after 
the first request in a 10-second window.
"""

import re
from datetime import datetime, timedelta
from collections import defaultdict

# Step 1: Read all lines from the log file into memory
with open('NodeJsApp.log', 'r') as file:
    log_lines = file.readlines()

# Step 2: Dictionary to hold lists of request timestamps per IP address
# Using defaultdict allows us to append timestamps without initializing each key
ip_requests = defaultdict(list)

# Step 3: Regular expression to extract:
# - IP address (appears after the initial ISO timestamp)
# - Timestamp (found inside square brackets in format: 03/Jun/2025:10:09:02 +0000)
log_pattern = r'^\S+\s+(\d+\.\d+\.\d+\.\d+).*?\[([^\]]+)\]'

# Step 4: Iterate through each log line and extract relevant data
for line in log_lines:
    match = re.match(log_pattern, line.strip())
    if match:
        ip_address = match.group(1)           # Extract the IP address
        timestamp_str = match.group(2)        # Extract the timestamp from inside brackets

        try:
            # Remove the timezone (if any) and parse the timestamp string to a datetime object
            # Example input: "03/Jun/2025:10:09:02 +0000"
            timestamp_clean = timestamp_str.split(' ')[0]  # Remove "+0000"
            timestamp = datetime.strptime(timestamp_clean, '%d/%b/%Y:%H:%M:%S')
            
            # Store the timestamp under the corresponding IP
            ip_requests[ip_address].append(timestamp)
        except ValueError as e:
            # Handle malformed timestamp entries (skip line and print error)
            print(f"Skipping due to timestamp error: {timestamp_str} — {e}")
            continue
    else:
        # Line didn't match expected format (e.g., malformed or unusual entry)
        print(f"No match for line: {line.strip()}")  # For debugging purposes

# Step 5: Analyze the requests for each IP to count how many occurred within 10 seconds after the first
results = {}  # Final output: IP → number of requests after the first one in a 10s window

for ip, timestamps in ip_requests.items():
    timestamps.sort()  # Sort timestamps to ensure chronological order

    if len(timestamps) < 2:
        # If there's only one request, then no "follow-up" requests to count
        results[ip] = 0
        continue

    # Define the time window: 10 seconds after the first request
    first_request = timestamps[0]
    window_end = first_request + timedelta(seconds=10)

    # Count how many subsequent requests (after the first) fall within that 10-second window
    requests_in_window = sum(1 for ts in timestamps[1:] if ts <= window_end)

    results[ip] = requests_in_window  # Store result for this IP

# Step 6: Write the results to an output file
with open('ip_request_analysis.txt', 'w') as output_file:
    output_file.write("IP Address Request Analysis - 10 Second Window\n")
    output_file.write("=" * 50 + "\n\n")
    
    # Sort IPs alphabetically for consistent and readable output
    for ip in sorted(results.keys()):
        count = results[ip]
        output_file.write(f"{ip}: {count} requests after first request in 10-second window\n")

# Inform the user that analysis is complete
print("Analysis complete. Results saved to 'ip_request_analysis.txt'")
