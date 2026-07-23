# Threat-Watch

Threat-Watch is a beginner-friendly cybersecurity project built with Python to simulate basic Security Operations Center (SOC) log analysis. It parses authentication logs, detects suspicious login activity, and identifies possible brute-force attacks.

## Features

- Parse authentication log files
- Display log events in a readable format
- Count failed login attempts per IP address
- Detect suspicious IP addresses
- Classify threats by severity
- Display a threat detection summary

## Project Progress

### Sprint 1 – Log Parsing
- Created sample authentication logs
- Parsed log entries into Python dictionaries
- Displayed events in a readable format

### Sprint 2 – Threat Detection
- Imported parser into the detection module
- Counted failed login attempts per IP address
- Generated alerts for IP addresses with multiple failed login attempts

### Sprint 3– Threat Intelligence
- Added threat severity classification
- Improved alert formatting
- Added threat summary dashboard
- Classified suspicious and high-risk IP addresses

## Project Structure

```
Threat-Watch/
│
├── logs/
│   └── sample.log
│
├── src/
│   ├── parser.py
│   └── Detection.py
│
├── screenshots/
│   ├── Sprint1/
│   ├── Sprint2/
│   └── Sprint4/
│
├── README.md
└── main.py
```

## Technologies Used

- Python
- Dictionaries
- Lists
- Loops
- Functions
- File Handling

## Future Improvements

- Generate `alerts.txt` incident reports
- Export reports to CSV
- Detect multiple attack types
- Add configurable alert thresholds
- Build a command-line interface (CLI)

## Author

**Uchenna Wisdom**

Cybersecurity Student | Python Learner | Aspiring Cybersecurity Architect