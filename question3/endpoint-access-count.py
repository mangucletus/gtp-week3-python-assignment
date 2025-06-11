#!/usr/bin/env python3
"""
Question 3: Count the number of times each endpoint was accessed.
"""

import re
from collections import defaultdict

# Read the log file
with open('NodeJsApp.log', 'r') as file:
    log_lines = file.readlines()

# Dictionary to count endpoint accesses
endpoint_counts = defaultdict(int)

# Regular expression to extract HTTP method and endpoint
# Assumes format: ... "GET /endpoint HTTP/1.1" ...
http_request_pattern = r'"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+([^\s]+)'

# Parse each log line to extract endpoints
for line in log_lines:
    line = line.strip()
    
    # Search for HTTP request pattern in the log line
    match = re.search(http_request_pattern, line)
    
    if match:
        http_method = match.group(1)
        endpoint = match.group(2)
        
        # Clean up the endpoint (remove query parameters for grouping)
        # Split by '?' to remove query string
        clean_endpoint = endpoint.split('?')[0]
        
        # Create a key that includes both method and endpoint
        request_key = f"{http_method} {clean_endpoint}"
        
        # Count this endpoint access
        endpoint_counts[request_key] += 1

# Also count just endpoints (without HTTP method) for summary
endpoint_only_counts = defaultdict(int)
for line in log_lines:
    line = line.strip()
    match = re.search(http_request_pattern, line)
    
    if match:
        endpoint = match.group(2)
        clean_endpoint = endpoint.split('?')[0]
        endpoint_only_counts[clean_endpoint] += 1

# Write results to output file
with open('endpoint_access_analysis.txt', 'w') as output_file:
    output_file.write("Endpoint Access Analysis\n")
    output_file.write("=" * 30 + "\n\n")
    
    # Write summary by endpoint (method + path)
    output_file.write("Access Count by Method and Endpoint:\n")
    output_file.write("-" * 40 + "\n")
    
    # Sort by count (descending) to show most accessed endpoints first
    sorted_endpoints = sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True)
    
    total_requests = sum(endpoint_counts.values())
    
    for endpoint, count in sorted_endpoints:
        # Calculate percentage of total requests
        percentage = (count / total_requests * 100) if total_requests > 0 else 0
        output_file.write(f"{count:6d} requests ({percentage:5.1f}%) - {endpoint}\n")
    
    # Write summary by endpoint only (ignoring HTTP method)
    output_file.write(f"\n\nAccess Count by Endpoint Only (ignoring HTTP method):\n")
    output_file.write("-" * 50 + "\n")
    
    # Sort endpoint-only counts by access count (descending)
    sorted_endpoint_only = sorted(endpoint_only_counts.items(), key=lambda x: x[1], reverse=True)
    
    for endpoint, count in sorted_endpoint_only:
        percentage = (count / total_requests * 100) if total_requests > 0 else 0
        output_file.write(f"{count:6d} requests ({percentage:5.1f}%) - {endpoint}\n")
    
    # Write summary statistics
    output_file.write(f"\n\nSummary Statistics:\n")
    output_file.write("-" * 20 + "\n")
    output_file.write(f"Total requests analyzed: {total_requests}\n")
    output_file.write(f"Unique endpoints (with method): {len(endpoint_counts)}\n")
    output_file.write(f"Unique endpoints (path only): {len(endpoint_only_counts)}\n")

print("Endpoint analysis complete. Results saved to 'endpoint_access_analysis.txt'")