import re  # Import the 're' module for using regular expressions

# Define the path to the input log file which contains log data
input_log_file = 'NodeJsApp.log'

# Define the path to the output log file where unique IP addresses will be saved
output_log_file = 'unique_ips.log'

# Define a regular expression pattern to match IPv4 addresses
# Explanation: 
#   - [0-9]{1,3} matches 1 to 3 digits
#   - (?: ... ){3} repeats the pattern of digits followed by a dot three times
#   - \b ensures word boundaries (only full IPs are matched)
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Create an empty set to store unique IP addresses
# Using a set automatically removes duplicates as sets do not allow repeated values
unique_ips = set()

# Open the input log file in read mode
with open(input_log_file, 'r') as file:
    # Read the file line by line
    for line in file:
        # Use the regular expression to find all IP addresses in the current line
        ips_in_line = re.findall(ip_pattern, line)

        # Add all found IPs to the set of unique IPs
        # 'update' adds multiple items at once to the set
        unique_ips.update(ips_in_line)

# Open the output log file in write mode
# This will overwrite the file if it already exists
with open(output_log_file, 'w') as output:
    # Iterate over the sorted list of unique IPs
    for ip in sorted(unique_ips):
        # Write each IP address to the output file, followed by a newline
        output.write(ip + '\n')

# Print a confirmation message to the console with the number of unique IPs found
print(f"Found {len(unique_ips)} unique IP address(es). Saved to '{output_log_file}'.")
