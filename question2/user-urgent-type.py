#!/usr/bin/env python3
"""
Question 2: Determine the number of requests coming from each user agent type.
"""

import re
from collections import defaultdict

# Read the log file
with open('NodeJsApp.log', 'r') as file:
    log_lines = file.readlines()

# Dictionary to count requests by user agent
user_agent_counts = defaultdict(int)

# Regular expression to extract user agent from log entries
# Assumes format: ... "user-agent-string"
# User agent typically appears at the end of log lines in quotes
user_agent_pattern = r'"([^"]*)"[^"]*$'

# Parse each log line to extract user agent
for line in log_lines:
    line = line.strip()
    
    # Look for user agent string (usually the last quoted string)
    matches = re.findall(r'"([^"]*)"', line)
    
    if matches and len(matches) >= 2:
        # User agent is typically the last quoted field after the HTTP request
        user_agent = matches[-1]
        
        # Skip empty user agents or ones that look like HTTP requests
        if user_agent and not user_agent.startswith(('GET', 'POST', 'PUT', 'DELETE')):
            # Classify user agent type based on common patterns
            user_agent_lower = user_agent.lower()
            
            # Determine user agent type/category
            if 'chrome' in user_agent_lower:
                agent_type = 'Chrome Browser'
            elif 'firefox' in user_agent_lower:
                agent_type = 'Firefox Browser'
            elif 'safari' in user_agent_lower and 'chrome' not in user_agent_lower:
                agent_type = 'Safari Browser'
            elif 'edge' in user_agent_lower:
                agent_type = 'Edge Browser'
            elif 'bot' in user_agent_lower or 'crawler' in user_agent_lower:
                agent_type = 'Bot/Crawler'
            elif 'mobile' in user_agent_lower or 'android' in user_agent_lower or 'iphone' in user_agent_lower:
                agent_type = 'Mobile Device'
            elif 'curl' in user_agent_lower or 'wget' in user_agent_lower:
                agent_type = 'Command Line Tool'
            elif 'postman' in user_agent_lower:
                agent_type = 'API Testing Tool'
            else:
                agent_type = 'Other/Unknown'
            
            # Count the classified user agent type
            user_agent_counts[agent_type] += 1

# Also keep track of exact user agent strings for detailed analysis
exact_user_agents = defaultdict(int)
for line in log_lines:
    line = line.strip()
    matches = re.findall(r'"([^"]*)"', line)
    
    if matches and len(matches) >= 2:
        user_agent = matches[-1]
        if user_agent and not user_agent.startswith(('GET', 'POST', 'PUT', 'DELETE')):
            exact_user_agents[user_agent] += 1

# Write results to output file
with open('user_agent_analysis.txt', 'w') as output_file:
    output_file.write("User Agent Analysis\n")
    output_file.write("=" * 30 + "\n\n")
    
    # Write summary by user agent type
    output_file.write("Summary by User Agent Type:\n")
    output_file.write("-" * 30 + "\n")
    
    # Sort by count (descending) for better readability
    sorted_types = sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True)
    
    for agent_type, count in sorted_types:
        output_file.write(f"{agent_type}: {count} requests\n")
    
    # Write detailed breakdown of exact user agent strings
    output_file.write("\n\nDetailed Breakdown (Exact User Agent Strings):\n")
    output_file.write("-" * 50 + "\n")
    
    # Sort exact user agents by count (descending)
    sorted_exact = sorted(exact_user_agents.items(), key=lambda x: x[1], reverse=True)
    
    for user_agent, count in sorted_exact:
        # Truncate very long user agent strings for readability
        display_agent = user_agent[:100] + "..." if len(user_agent) > 100 else user_agent
        output_file.write(f"{count} requests: {display_agent}\n")

print("User agent analysis complete. Results saved to 'user_agent_analysis.txt'")