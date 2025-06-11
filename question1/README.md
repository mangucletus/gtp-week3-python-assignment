# Web Server Log Analysis 

A Python script that analyzes web server log files to identify IP addresses with high request frequency within short time windows. This tool helps detect potential suspicious activity, bot traffic, or unusual access patterns by counting how many requests each IP address makes within 10 seconds of their first request.

## Features

- Parses web server log files in Apache/Nginx common log format
- Extracts IP addresses and timestamps from log entries
- Counts subsequent requests within a 10-second window for each IP
- Generates a sorted analysis report
- Handles malformed log entries gracefully
- Provides detailed error reporting for debugging

## Requirements

- Python 3.6 or higher
- Standard Python libraries (no additional dependencies required):
  - `re` (regular expressions)
  - `datetime` (date/time handling)
  - `collections` (defaultdict)

## Installation

1. Clone or download the script to your local machine
2. Ensure you have Python 3.6+ installed
3. Place your log file in the same directory as the script

## Usage

### Basic Usage

```bash
python3 ip-address-request-window.py
```

### Prerequisites

1. Ensure your log file is named `NodeJsApp.log` and is in the same directory as the script
2. The log file should follow the standard web server log format

### Expected Log Format

The script expects log entries in the following format:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0..."
```

Key components:
- **ISO Timestamp**: `2025-06-03T10:09:02.588Z`
- **IP Address**: `197.159.135.110`
- **Bracketed Timestamp**: `[03/Jun/2025:10:09:02 +0000]`
- **HTTP Request Details**: Method, path, protocol, status code, etc.

## Output

The script generates a file called `ip_request_analysis.txt` containing:
- Analysis header
- IP addresses sorted alphabetically
- Count of requests made within 10 seconds of each IP's first request

### Sample Output
```
IP Address Request Analysis - 10 Second Window
==================================================

129.222.148.186: 8 requests after first request in 10-second window
154.161.141.194: 21 requests after first request in 10-second window
154.161.35.247: 8 requests after first request in 10-second window
154.161.40.25: 5 requests after first request in 10-second window
185.195.59.88: 19 requests after first request in 10-second window
196.61.35.158: 15 requests after first request in 10-second window
197.159.135.110: 2 requests after first request in 10-second window
```

## How It Works

1. **Log Parsing**: Reads the entire log file into memory and processes each line
2. **Pattern Matching**: Uses regex to extract IP addresses and timestamps from log entries
3. **Data Grouping**: Groups all requests by IP address using a defaultdict
4. **Time Window Analysis**: For each IP:
   - Sorts requests chronologically
   - Identifies the first request timestamp
   - Counts subsequent requests within a 10-second window
5. **Report Generation**: Creates a sorted report of all analyzed IP addresses

### Algorithm Details

- **Time Window**: 10 seconds from the first request timestamp
- **Counting Logic**: Only counts requests that occur AFTER the first request
- **Sorting**: Results are sorted alphabetically by IP address for consistency

## Use Cases

- **Security Analysis**: Identify potential DDoS attacks or bot traffic
- **Traffic Pattern Analysis**: Understand user behavior and request patterns
- **Performance Monitoring**: Detect unusual spikes in activity
- **Rate Limiting**: Identify IPs that may need throttling

## File Structure

```
question1/
├── ip-address-request-window.py          # Main analysis script
├── NodeJsApp.log           # Input log file (required)
├── ip_request_analysis.txt # Output analysis report (generated)
└── README.md               # This documentation
```

## Error Handling

The script includes robust error handling for:
- **Malformed Timestamps**: Skips entries with invalid date formats
- **Regex Mismatches**: Reports lines that don't match expected format
- **File Access Issues**: Handles missing input files gracefully

### Debugging Output

During execution, the script may display:
- Timestamp parsing errors with specific error messages
- Lines that don't match the expected log format
- Completion confirmation message

## Customization

### Modifying the Time Window

To change the analysis window from 10 seconds to another duration, modify this line:
```python
window_end = first_request + timedelta(seconds=10)  # Change 10 to desired seconds
```

### Changing Input/Output Files

Update these file references in the script:
```python
with open('NodeJsApp.log', 'r') as file:        # Input file
with open('ip_request_analysis.txt', 'w') as output_file:  # Output file
```

### Adjusting Log Format

If your log format differs, modify the regex pattern:
```python
log_pattern = r'^\S+\s+(\d+\.\d+\.\d+\.\d+).*?\[([^\]]+)\]'
```

## Troubleshooting

### Common Issues

1. **File Not Found**: Ensure `NodeJsApp.log` exists in the script directory
2. **No Output**: Check if log file contains entries matching the expected format
3. **Timestamp Errors**: Verify log timestamps follow the format `dd/Mon/yyyy:HH:MM:SS +ZZZZ`

### Performance Considerations

- **Memory Usage**: Script loads entire log file into memory
- **Large Files**: For very large log files (>1GB), consider processing in chunks
- **Processing Time**: Execution time scales linearly with log file size

