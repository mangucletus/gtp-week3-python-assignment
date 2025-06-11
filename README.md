# GTP Week 3 Python Assignment - Web Server Log Analysis

A comprehensive collection of Python scripts designed to analyze web server log files and extract valuable insights about traffic patterns, security threats, and user behavior. This assignment demonstrates three complementary analysis tools that work together to give you a complete picture of your web server's activity.

##  Analysis Tools Overview

### 1. **IP Address Request Analysis** (`ip-address-request-window.py`) - Question 1
**Purpose**: Identifies potential suspicious activity by analyzing request frequency patterns
- Counts requests within 10-second windows for each IP address
- Detects potential DDoS attacks, bot traffic, or automated scraping
- Helps identify IPs that may need rate limiting or blocking

### 2. **User Agent Analysis** (`user-agent-type.py`) - Question 2
**Purpose**: Categorizes and analyzes the types of clients accessing your server
- Classifies browsers, mobile devices, bots, and API tools
- Provides insights into your audience's technology preferences
- Helps detect automated traffic and security threats

### 3. **Endpoint Access Analysis** (`endpoint-access-count.py`) - Question 3
**Purpose**: Tracks which resources and API endpoints are most frequently accessed
- Monitors endpoint popularity and usage patterns
- Identifies optimization opportunities for high-traffic resources
- Supports performance tuning and caching strategies

##  Quick Start

### Prerequisites
- Python 3.6 or higher
- Web server log file named `NodeJsApp.log` in each question directory

### Installation
```bash
# Clone or download the assignment
git clone <repository-url>
cd gtp-week3-python-assignment

# Ensure log files exist in each question directory
ls question1/NodeJsApp.log
ls question2/NodeJsApp.log
ls question3/NodeJsApp.log
```

### Running All Analyses
```bash
# Navigate to each question directory and run the analysis

# Question 1: IP Address Request Analysis
cd question1
python3 ip-address-request-window.py
cat ip_request_analysis.txt

# Question 2: User Agent Analysis
cd ../question2
python3 user-agent-type.py
cat user_agent_analysis.txt

# Question 3: Endpoint Access Analysis
cd ../question3
python3 endpoint-access-count.py
cat endpoint_access_analysis.txt
```

## 📁 Project Structure

```
gtp-week3-python-assignment/
├── README.md                          # This overview document
│
├── question1/                         # IP Address Request Analysis
│   ├── NodeJsApp.log                 # Web server log file
│   ├── ip-address-request-window.py   # IP request pattern analysis script
│   ├── ip_request_analysis.txt        # IP analysis results (generated)
│   └── README.md                      # Detailed IP analysis documentation
│
├── question2/                         # User Agent Analysis
│   ├── NodeJsApp.log                 # Web server log file
│   ├── user-agent-type.py            # User agent categorization script
│   ├── user_agent_analysis.txt       # User agent results (generated)
│   └── README.md                      # Detailed user agent documentation
│
└── question3/                         # Endpoint Access Analysis
    ├── NodeJsApp.log                 # Web server log file
    ├── endpoint-access-count.py       # Endpoint usage tracking script
    ├── endpoint_access_analysis.txt   # Endpoint results (generated)
    └── README.md                      # Detailed endpoint analysis documentation
```

##  Sample Results Overview

Based on a sample analysis of 724 total requests:

### IP Analysis Results
```
129.222.148.186: 8 requests after first request in 10-second window
154.161.141.194: 21 requests after first request in 10-second window
154.161.35.247: 8 requests after first request in 10-second window
```
**Insight**: IP `154.161.141.194` shows high request frequency, warranting investigation.

### User Agent Results
```
Chrome Browser: 640 requests (88.4%)
Safari Browser: 84 requests (11.6%)
```
**Insight**: Predominantly legitimate browser traffic with Chrome dominating usage.

### Endpoint Results
```
408 requests (56.4%) - GET /
316 requests (43.6%) - GET /favicon.ico
```
**Insight**: Simple application with two main endpoints, typical home page and favicon pattern.

##  Use Cases & Applications

### Security Monitoring
- **Threat Detection**: IP analysis identifies potential attacks or unusual activity
- **Bot Identification**: User agent analysis reveals automated traffic
- **Access Pattern Monitoring**: Endpoint analysis shows if attackers are probing specific resources

### Performance Optimization
- **Caching Strategy**: Endpoint analysis guides caching decisions for high-traffic resources
- **Load Balancing**: IP patterns help distribute traffic effectively
- **Browser Optimization**: User agent data informs browser compatibility priorities

### Business Intelligence
- **User Demographics**: Understand your audience's technology preferences
- **Feature Usage**: Track which parts of your application are most popular
- **Growth Planning**: Identify trends and plan infrastructure scaling

### Compliance & Auditing
- **Access Logging**: Comprehensive request tracking for audit trails
- **Pattern Documentation**: Evidence of normal vs. abnormal traffic patterns
- **Incident Investigation**: Tools to analyze suspicious activity periods

##  Advanced Usage

### Automated Analysis Pipeline
Create a script to run all analyses automatically:

```bash
#!/bin/bash
# run_analysis.sh

echo "Starting GTP Week 3 Python Assignment Analysis..."

echo "1. Analyzing IP request patterns (Question 1)..."
cd question1
python3 ip-address-request-window.py
cd ..

echo "2. Analyzing user agents (Question 2)..."
cd question2
python3 user-agent-type.py
cd ..

echo "3. Analyzing endpoint usage (Question 3)..."
cd question3
python3 endpoint-access-count.py
cd ..

echo "Analysis complete! Check the generated .txt files in each question directory."
```

### Integration with Monitoring Systems
```python
# Example: Send alerts for suspicious activity
import subprocess
import smtplib
import os

def check_for_threats():
    # Run IP analysis
    os.chdir('question1')
    subprocess.run(['python3', 'ip-address-request-window.py'])
    
    # Parse results and check for high request counts
    with open('ip_request_analysis.txt', 'r') as f:
        if any('20' in line for line in f):  # 20+ requests in 10 seconds
            send_alert("Potential DDoS detected!")
    
    os.chdir('..')

def send_alert(message):
    # Implement your alerting mechanism
    pass
```

### Custom Report Generation
```python
# combine_reports.py
def generate_summary_report():
    """Combine all three analyses into a single summary report."""
    
    with open('security_summary.txt', 'w') as summary:
        summary.write("WEB SERVER SECURITY & TRAFFIC SUMMARY\n")
        summary.write("=" * 50 + "\n\n")
        
        # Include top findings from each analysis
        # Add executive summary and recommendations
        # Highlight security concerns and optimization opportunities
```

##  Configuration Options

### Log File Format
All scripts expect standard web server log format:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "referrer" "user-agent"
```

### Customizing Analysis Parameters

**IP Analysis Window**: Change the time window from 10 seconds:
```python
# In ip_analyzer.py
window_end = first_request + timedelta(seconds=30)  # 30-second window
```

**User Agent Categories**: Add new browser or tool detection:
```python
# In user_agent_analyzer.py
elif 'opera' in user_agent_lower:
    agent_type = 'Opera Browser'
```

**Endpoint Grouping**: Modify how endpoints are grouped:
```python
# In endpoint_analyzer.py
# Keep query parameters instead of removing them
clean_endpoint = endpoint  # Don't split on '?'
```

##  Troubleshooting

### Common Issues

1. **No Results Generated**
   - Verify `NodeJsApp.log` exists in the respective question directory
   - Check file permissions and Python version
   - Review log format compatibility

2. **Unexpected Results**
   - Examine sample log entries for format variations
   - Check regex patterns in each script
   - Validate timestamp and date formats

3. **Performance Issues**
   - For large log files (>100MB), consider processing in chunks
   - Monitor memory usage during analysis
   - Consider running analyses separately for large datasets

### Log Format Compatibility

The scripts work with most standard web server logs including:
- **Apache Common Log Format**
- **Apache Combined Log Format**
- **Nginx default log format**
- **Custom formats** (may require regex modifications)

##  Interpreting Combined Results

### Security Assessment
- **High IP request counts** + **Bot user agents** + **Unusual endpoints** = Potential attack
- **Normal IP patterns** + **Browser user agents** + **Standard endpoints** = Legitimate traffic

### Performance Insights
- **Popular endpoints** from endpoint analysis guide caching priorities
- **Browser distribution** from user agent analysis informs testing priorities
- **Request patterns** from IP analysis help predict traffic loads

### Business Intelligence
- **User agent trends** reveal your audience's technology preferences
- **Endpoint popularity** shows which features users value most
- **Geographic patterns** (from IP analysis) guide expansion decisions

##  Security Alerts

Set up monitoring based on these thresholds:

| Metric | Normal Range | Alert Threshold | Action |
|--------|--------------|-----------------|---------|
| IP requests/10s | 1-5 | >15 | Investigate potential bot/attack |
| Bot percentage | <10% | >30% | Review traffic legitimacy |
| Unknown user agents | <5% | >20% | Check for new threat vectors |
| Error endpoint hits | <1% | >10% | Investigate potential probing |

##  Documentation

For detailed information about each analysis tool:
- **Question 1 - IP Analysis**: See `question1/README.md`
- **Question 2 - User Agent Analysis**: See `question2/README.md`
- **Question 3 - Endpoint Analysis**: See `question3/README.md`

