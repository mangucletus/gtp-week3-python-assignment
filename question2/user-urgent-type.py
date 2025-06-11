#!/usr/bin/env python3
"""
Question 2: Determine the number of requests coming from each user agent type.
"""

import re
from collections import defaultdict

# Step 1: Read the entire log file into memory
with open('NodeJsApp.log', 'r') as file:
    log_lines = file.readlines()

# Step 2: Initialize a dictionary to hold counts of each user agent type
# defaultdict(int) simplifies incrementing keys that aren't initialized yet
user_agent_counts = defaultdict(int)

# Step 3: Regular expression to extract quoted strings, especially the user agent
# The user agent is typically the last quoted string in each log line
user_agent_pattern = r'"([^"]*)"[^"]*$'  # (Note: defined but not used; extraction done via re.findall below)

# Step 4: Parse each log line to classify and count user agent types
for line in log_lines:
    line = line.strip()  # Remove leading/trailing whitespace
    
    # Extract all quoted fields using regex (e.g., HTTP request, referrer, user agent)
    matches = re.findall(r'"([^"]*)"', line)
    
    if matches and len(matches) >= 2:
        # By convention, the user agent is the last quoted string in most log formats
        user_agent = matches[-1]
        
        # Ensure it's not empty and doesn't mistakenly capture HTTP verbs
        if user_agent and not user_agent.startswith(('GET', 'POST', 'PUT', 'DELETE')):
            # Normalize the string for easier matching
            user_agent_lower = user_agent.lower()
            
            # Classify user agent type based on signature keywords
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
                agent_type = 'Other/Unknown'  # Catch-all for unrecognized user agents
            
            # Increment the count for the identified agent type
            user_agent_counts[agent_type] += 1

# Step 5: (Optional) Gather exact user agent strings for a detailed breakdown
exact_user_agents = defaultdict(int)

for line in log_lines:
    line = line.strip()
    matches = re.findall(r'"([^"]*)"', line)
    
    if matches and len(matches) >= 2:
        user_agent = matches[-1]
        
        # Avoid counting non-agent strings
        if user_agent and not user_agent.startswith(('GET', 'POST', 'PUT', 'DELETE')):
            exact_user_agents[user_agent] += 1  # Increment count of exact user agent string

# Step 6: Write both the summary and detailed analysis to an output file
with open('user_agent_analysis.txt', 'w') as output_file:
    output_file.write("User Agent Analysis\n")
    output_file.write("=" * 30 + "\n\n")
    
    # Section: Summary by user agent type (e.g., Chrome, Firefox, etc.)
    output_file.write("Summary by User Agent Type:\n")
    output_file.write("-" * 30 + "\n")
    
    # Sort by number of requests (descending) for better readability
    sorted_types = sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True)
    
    for agent_type, count in sorted_types:
        output_file.write(f"{agent_type}: {count} requests\n")
    
    # Section: Detailed breakdown of each exact user agent string
    output_file.write("\n\nDetailed Breakdown (Exact User Agent Strings):\n")
    output_file.write("-" * 50 + "\n")
    
    # Sort exact strings by frequency (descending)
    sorted_exact = sorted(exact_user_agents.items(), key=lambda x: x[1], reverse=True)
    
    for user_agent, count in sorted_exact:
        # Truncate very long user agents for readability in the output
        display_agent = user_agent[:100] + "..." if len(user_agent) > 100 else user_agent
        output_file.write(f"{count} requests: {display_agent}\n")

# Final message for the user
print("User agent analysis complete. Results saved to 'user_agent_analysis.txt'")
