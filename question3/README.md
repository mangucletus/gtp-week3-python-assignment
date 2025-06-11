# Endpoint Access Analysis 

A Python script that analyzes web server log files to track and count endpoint usage patterns. This tool helps understand which API endpoints, pages, and resources are most frequently accessed, providing valuable insights for performance optimization, resource allocation, and API usage monitoring.

## Features

- Parses web server log files to extract HTTP methods and endpoints
- Counts access frequency for each endpoint with percentage breakdowns
- Provides dual analysis: method+endpoint combinations and endpoint-only statistics
- Removes query parameters for cleaner grouping and analysis
- Generates comprehensive reports with summary statistics
- Supports all standard HTTP methods (GET, POST, PUT, DELETE, etc.)
- Calculates usage percentages for easy interpretation

## Requirements

- Python 3.6 or higher
- Standard Python libraries (no additional dependencies required):
  - `re` (regular expressions)
  - `collections` (defaultdict)

## Installation

1. Clone or download the script to your local machine
2. Ensure you have Python 3.6+ installed
3. Place your log file in the same directory as the script

## Usage

### Basic Usage

```bash
python3 endpoint-access-count.py
```

### Prerequisites

1. Ensure your log file is named `NodeJsApp.log` and is in the same directory as the script
2. The log file should contain HTTP request information in quoted fields

### Expected Log Format

The script expects log entries with HTTP requests in quotes:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
```

Key components the script extracts:
- **HTTP Method**: GET, POST, PUT, DELETE, etc.
- **Endpoint Path**: The URL path being accessed
- **Protocol Version**: HTTP/1.1, HTTP/2, etc. (for validation)

## Output

The script generates a file called `endpoint_access_analysis.txt` containing three main sections:

### 1. Access Count by Method and Endpoint
Shows the complete request breakdown including HTTP method:
```
   408 requests ( 56.4%) - GET /
   316 requests ( 43.6%) - GET /favicon.ico
```

### 2. Access Count by Endpoint Only
Groups requests by path regardless of HTTP method:
```
   408 requests ( 56.4%) - /
   316 requests ( 43.6%) - /favicon.ico
```

### 3. Summary Statistics
Provides overall analysis metrics:
```
Total requests analyzed: 724
Unique endpoints (with method): 2
Unique endpoints (path only): 2
```

### Sample Complete Output
```
Endpoint Access Analysis
==============================

Access Count by Method and Endpoint:
----------------------------------------
   408 requests ( 56.4%) - GET /
   316 requests ( 43.6%) - GET /favicon.ico

Access Count by Endpoint Only (ignoring HTTP method):
--------------------------------------------------
   408 requests ( 56.4%) - /
   316 requests ( 43.6%) - /favicon.ico

Summary Statistics:
--------------------
Total requests analyzed: 724
Unique endpoints (with method): 2
Unique endpoints (path only): 2
```

## How It Works

### Algorithm Overview

1. **Log Parsing**: Reads the entire log file line by line
2. **Request Extraction**: Uses regex to identify HTTP request patterns within quoted strings
3. **Endpoint Cleaning**: Removes query parameters (everything after '?') for cleaner grouping
4. **Dual Counting**: Maintains separate counts for method+endpoint and endpoint-only statistics
5. **Statistical Calculation**: Computes percentages and summary metrics
6. **Report Generation**: Creates sorted output with most accessed endpoints first

### HTTP Method Detection

The script recognizes standard HTTP methods:
- **GET**: Retrieving data or resources
- **POST**: Creating new resources or submitting data
- **PUT**: Updating existing resources
- **DELETE**: Removing resources
- **PATCH**: Partial updates
- **HEAD**: Metadata requests
- **OPTIONS**: Preflight and capability checks

### Query Parameter Handling

The script automatically removes query parameters to group similar requests:
```python
# Before: /api/users?id=123&filter=active
# After:  /api/users
clean_endpoint = endpoint.split('?')[0]
```

This ensures that `/api/users?id=1` and `/api/users?id=2` are counted as the same endpoint.

## Use Cases

### API Development & Monitoring
- **Endpoint Popularity**: Identify most and least used API endpoints
- **Method Distribution**: Understand the balance between GET, POST, PUT, DELETE operations
- **Resource Optimization**: Focus performance improvements on high-traffic endpoints
- **Deprecation Planning**: Identify unused endpoints for potential removal

### Website Analytics
- **Page Popularity**: Track which pages users visit most frequently
- **Resource Usage**: Monitor static asset requests (CSS, JS, images)
- **User Journey**: Understand navigation patterns through endpoint access

### Performance Optimization
- **Caching Strategy**: Prioritize caching for frequently accessed endpoints
- **Load Balancing**: Distribute traffic based on endpoint usage patterns
- **Database Optimization**: Optimize queries for high-traffic endpoints
- **CDN Configuration**: Identify static resources for CDN delivery

### Security & Compliance
- **Access Patterns**: Monitor for unusual endpoint access patterns
- **Attack Detection**: Identify potential reconnaissance or brute force attempts
- **Audit Trails**: Track API usage for compliance requirements
- **Rate Limiting**: Implement limits based on actual usage patterns

## File Structure

```
question3/
├── endpoint-access-count.py           # Main analysis script
├── NodeJsApp.log                 # Input log file (required)
├── endpoint_access_analysis.txt  # Output analysis report (generated)
└── README.md                     # This documentation
```

## Configuration Options

### Customizing HTTP Methods

Add support for additional HTTP methods by modifying the regex pattern:
```python
http_request_pattern = r'"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS|CONNECT|TRACE)\s+([^\s]+)'
```

### Changing Query Parameter Handling

Modify how query parameters are handled:
```python
# Keep query parameters
clean_endpoint = endpoint

# Remove only specific parameters
clean_endpoint = re.sub(r'[?&]id=\d+', '', endpoint)

# Keep first parameter only
clean_endpoint = endpoint.split('&')[0]
```

### Adjusting Output Format

Customize the output formatting:
```python
# Change decimal places for percentages
output_file.write(f"{count:6d} requests ({percentage:6.2f}%) - {endpoint}\n")

# Add request rate calculations
rate_per_minute = count / total_time_minutes
output_file.write(f"{endpoint}: {rate_per_minute:.1f} req/min\n")
```

### File Path Configuration

Update input and output file paths:
```python
with open('NodeJsApp.log', 'r') as file:              # Input file
with open('endpoint_access_analysis.txt', 'w') as output_file:  # Output file
```

## Interpreting Results

### High Traffic Endpoints
- **Root Path (/)**: Usually indicates home page or health check requests
- **Static Assets**: High counts for CSS, JS, images are normal
- **API Endpoints**: Focus optimization efforts on frequently used APIs

### Low Traffic Endpoints
- **Rarely Used Features**: Consider whether maintenance cost is justified
- **Legacy Endpoints**: Candidates for deprecation
- **Error Pages**: Low counts are generally positive

### Method Distribution
- **GET Dominance**: Normal for most web applications and APIs
- **High POST/PUT**: Indicates active data manipulation
- **OPTIONS Requests**: Common with CORS-enabled APIs

### Performance Indicators
- **Even Distribution**: May indicate good load balancing
- **Heavy Concentration**: Might suggest optimization opportunities
- **Unexpected Patterns**: Could indicate bot traffic or attacks

## Advanced Analysis

### Combining with Other Tools

This endpoint analysis pairs well with:
- **IP Address Analysis**: Correlate endpoint usage with traffic sources
- **User Agent Analysis**: Understand which clients access which endpoints
- **Time-based Analysis**: Identify peak usage periods for endpoints

### Custom Metrics

Extend the analysis with additional calculations:
```python
# Calculate average requests per unique IP per endpoint
# Add response time analysis (if available in logs)
# Identify endpoint access sequences (user journeys)
# Monitor error rates by endpoint
```

## Troubleshooting

### Common Issues

1. **No Endpoints Detected**
   - Verify log format includes quoted HTTP requests
   - Check regex pattern matches your log structure
   - Ensure HTTP method keywords are recognized

2. **Unexpected Endpoint Names**
   - Review query parameter removal logic
   - Check for URL encoding issues
   - Verify endpoint path extraction accuracy

3. **Missing Requests**
   - Confirm all HTTP methods are included in regex
   - Check for case sensitivity issues
   - Validate log file completeness

### Performance Considerations

- **Memory Usage**: Stores all unique endpoint combinations
- **Processing Speed**: Linear with log file size
- **Output Size**: Grows with endpoint diversity

### Data Quality

- **Duplicate Entries**: Script handles naturally through counting
- **Malformed Requests**: Invalid HTTP methods are ignored
- **Incomplete Logs**: Only processes successfully parsed entries

## Security Considerations

### Sensitive Information
- **Query Parameters**: Removed by default to avoid logging sensitive data
- **API Keys**: Ensure logs don't contain authentication tokens
- **Personal Data**: Be mindful of privacy regulations when analyzing logs

### Attack Detection
- **Unusual Endpoints**: Monitor for requests to non-existent paths
- **Method Anomalies**: Watch for unexpected HTTP methods
- **Frequency Spikes**: Identify potential DDoS or scraping attempts

## Best Practices

### Regular Monitoring
- **Daily Analysis**: Track endpoint usage trends over time
- **Baseline Establishment**: Define normal usage patterns
- **Alert Thresholds**: Set up notifications for unusual activity

### Integration Ideas
- **Dashboard Integration**: Feed data into monitoring dashboards
- **Automated Reports**: Schedule regular analysis runs
- **Alerting Systems**: Trigger alerts on unusual patterns

