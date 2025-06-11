# User Agent Analysis 

A Python script that analyzes web server log files to categorize and count requests by user agent types. This tool helps understand your website's traffic composition, identify different browsers, devices, bots, and API tools accessing your server.

## Features

- Parses web server log files to extract user agent information
- Categorizes user agents into meaningful groups (browsers, mobile devices, bots, etc.)
- Provides both summary statistics and detailed breakdowns
- Handles various log formats with flexible regex parsing
- Generates comprehensive reports with request counts
- Identifies potential automated traffic and API usage

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
python3 user-agent-type.py
```

### Prerequisites

1. Ensure your log file is named `NodeJsApp.log` and is in the same directory as the script
2. The log file should contain user agent strings in quoted fields

### Expected Log Format

The script expects log entries with user agent strings in quotes:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
```

The user agent string is typically the last quoted field in each log entry.

## Output

The script generates a file called `user_agent_analysis.txt` containing:

### 1. Summary by User Agent Type
Categorized counts of requests by browser/tool type:
- **Chrome Browser**: Requests from Google Chrome
- **Firefox Browser**: Requests from Mozilla Firefox  
- **Safari Browser**: Requests from Apple Safari
- **Edge Browser**: Requests from Microsoft Edge
- **Bot/Crawler**: Automated crawlers and search engine bots
- **Mobile Device**: Mobile browsers and apps
- **Command Line Tool**: curl, wget, and similar tools
- **API Testing Tool**: Postman and similar applications
- **Other/Unknown**: Unclassified user agents

### 2. Detailed Breakdown
Exact user agent strings with their individual request counts, sorted by frequency.

### Sample Output
```
User Agent Analysis
==============================

Summary by User Agent Type:
------------------------------
Chrome Browser: 640 requests
Safari Browser: 84 requests

Detailed Breakdown (Exact User Agent Strings):
--------------------------------------------------
427 requests: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.3...
133 requests: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.3...
84 requests: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18....
42 requests: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0....
```

## How It Works

### Algorithm Overview

1. **Log Parsing**: Reads the entire log file and processes each line
2. **User Agent Extraction**: Uses regex to find quoted strings, identifying the user agent (typically the last quoted field)
3. **Classification**: Categorizes user agents based on keyword matching:
   - Browser detection (Chrome, Firefox, Safari, Edge)
   - Bot/crawler identification
   - Mobile device detection
   - Tool identification (curl, wget, Postman)
4. **Counting**: Maintains counts for both categories and exact strings
5. **Report Generation**: Creates sorted output with both summary and detailed views

### Classification Logic

The script uses keyword-based classification:
```python
if 'chrome' in user_agent_lower:
    agent_type = 'Chrome Browser'
elif 'bot' in user_agent_lower or 'crawler' in user_agent_lower:
    agent_type = 'Bot/Crawler'
elif 'mobile' in user_agent_lower or 'android' in user_agent_lower:
    agent_type = 'Mobile Device'
# ... additional classifications
```

## Use Cases

### Website Analytics
- **Traffic Composition**: Understand which browsers your users prefer
- **Mobile vs Desktop**: Identify mobile traffic patterns
- **Browser Compatibility**: Determine which browsers to prioritize for testing

### Security Monitoring
- **Bot Detection**: Identify automated traffic and potential scrapers
- **Unusual Activity**: Spot suspicious user agents or tools
- **API Usage**: Monitor programmatic access to your services

### Performance Optimization
- **Browser-Specific Issues**: Identify browsers that may need special handling
- **User Experience**: Tailor content delivery based on client capabilities
- **Resource Planning**: Understand traffic patterns for capacity planning

## File Structure

```
question2/
├── user-agent-type.py      # Main analysis script
├── NodeJsApp.log              # Input log file (required)
├── user_agent_analysis.txt    # Output analysis report (generated)
└── README.md                  # This documentation
```

## Configuration Options

### Customizing User Agent Categories

You can modify the classification logic by editing the keyword matching section:

```python
# Add new browser detection
elif 'opera' in user_agent_lower:
    agent_type = 'Opera Browser'

# Add new bot patterns
elif 'googlebot' in user_agent_lower or 'bingbot' in user_agent_lower:
    agent_type = 'Search Engine Bot'
```

### Changing Input/Output Files

Update these file references in the script:
```python
with open('NodeJsApp.log', 'r') as file:           # Input file
with open('user_agent_analysis.txt', 'w') as output_file:  # Output file
```

### Adjusting Output Format

Modify the output sections to change report formatting:
- Adjust truncation length for long user agent strings
- Change sorting criteria (alphabetical vs. count-based)
- Add percentage calculations

## Interpreting Results

### High Chrome/Safari Counts
- Normal for most websites
- Indicates standard web browser traffic
- Good sign of legitimate user engagement

### High Bot/Crawler Activity
- May indicate search engine indexing (positive)
- Could suggest scraping activity (monitor closely)
- Check if traffic aligns with your robots.txt

### Unusual User Agents
- Command line tools might indicate API usage
- Unknown agents could be custom applications
- Investigate patterns that seem suspicious

### Version Distribution
- Multiple browser versions are normal
- Very old versions might indicate security concerns
- Helps inform browser support decisions

## Troubleshooting

### Common Issues

1. **No Results Generated**
   - Check if log file exists and contains quoted strings
   - Verify log format matches expected structure
   - Look for parsing errors in console output

2. **Unexpected Categories**
   - Review classification logic for edge cases
   - Check for non-standard user agent formats
   - Consider expanding keyword patterns

3. **Memory Issues**
   - For very large log files, consider processing in chunks
   - Monitor system resources during execution

### Performance Considerations

- **Processing Speed**: Linear with log file size
- **Memory Usage**: Stores all unique user agent strings
- **Output Size**: Grows with unique user agent diversity

## Advanced Usage

### Combining with Other Analysis

This tool pairs well with:
- IP address analysis (for comprehensive traffic profiling)
- Time-based analysis (to identify traffic patterns)
- Response code analysis (to correlate user agents with errors)

### Automation Ideas

- Schedule regular analysis runs
- Set up alerts for unusual user agent patterns
- Integrate with monitoring dashboards
- Export data to analytics platforms

## Security Considerations

### Privacy
- User agent strings may contain identifying information
- Consider data retention policies for log analysis
- Be mindful of privacy regulations when sharing results

### Threat Detection
- Monitor for suspicious user agent patterns
- Look for attempts to disguise automated traffic
- Cross-reference with other security indicators
