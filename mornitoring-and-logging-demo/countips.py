#!/usr/bin/env python3

import re  # Import the 're' module for using regular expressions

# Define the path to the input log file which contains log data
input_log_file = 'NodeJsApp.log'

# Define the path to the output log file where IP address counts will be saved
output_log_file = 'ip_counts.log'

# Define a regular expression pattern to match IPv4 addresses
# Matches patterns like 192.168.0.1
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Create an empty dictionary to store IP address counts
ip_counts = {}

# Open the input log file in read mode
with open(input_log_file, 'r') as file:
    # Read the file line by line
    for line in file:
        # Use the regular expression to find all IP addresses in the current line
        ips_in_line = re.findall(ip_pattern, line)

        # Update counts for each IP found
        for ip in ips_in_line:
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

# Open the output log file in write mode (overwrite if exists)
with open(output_log_file, 'w') as output:
    # Iterate over sorted IPs and write them with their count
    for ip in sorted(ip_counts):
        output.write(f"{ip} {ip_counts[ip]}\n")

# Print a summary
print(f"Counted {len(ip_counts)} unique IP address(es). Saved to '{output_log_file}'.")

