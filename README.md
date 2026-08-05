Threat-Watch
Threat-Watch is a Python-based Security Operations Center (SOC) simulation that analyzes authentication logs, detects brute-force attacks, classifies threats by severity, and generates structured security reports.
Features
Parse authentication log files
Display log events in a readable format
Count failed login attempts per IP address
Detect suspicious IP addresses
Classify threats by severity
Generate threat reports in TXT and JSON formats
Interactive CLI menu for security log analysis
Project Progress
Sprint 1 – Log Parsing
Created sample authentication logs
Parsed log entries into Python dictionaries
Displayed events in a readable format
Sprint 2 – Threat Detection
Counted failed login attempts per IP address
Detected suspicious IP addresses
Generated brute-force alerts
Sprint 3 – Threat Intelligence
Implemented threat severity classification
Improved alert formatting
Added a threat detection summary
Classified suspicious and high-risk IP addresses
Sprint 4 – Threat Report Generation
Generated threat_report.txt
Exported detected threats to a report
Added report summaries
Sprint 5 – Interactive CLI
Built an interactive command-line menu
Enabled log analysis and report generation through the CLI
Sprint 6 – JSON Report Export
Stored detected threats using dictionaries and lists
Exported reports to threat_report.json
Sprint 7 – Error Handling
Added try/except blocks
Improved program stability
Displayed user-friendly error messages
Project Structure
Threat-Watch/
│
├── logs/
│   └── sample.log
│
├── reports/
│   ├── threat_report.txt
│   └── threat_report.json
│
├── src/
│   ├── parser.py
│   ├── detection.py
│   └── pydroid1.py
│
├── screenshots/
│   ├── Sprint1/
│   ├── Sprint2/
│   ├── Sprint3/
│   ├── Sprint4/
│   ├── Sprint5/
│   ├── Sprint6/
│   └── Sprint7/
│
├── README.md
└── main.py
Technologies Used
Python
JSON
File Handling
Dictionaries
Lists
Functions
Exception Handling
Command-Line Interface (CLI)
Future Improvements
[ ] AWS CloudTrail Integration
[ ] Amazon S3 Support
[ ] IAM Activity Monitoring
[ ] Email Alerting
[ ] Web Dashboard
[ ] Support for additional attack types
[ ] CSV Report Export
[ ] Configurable alert thresholds
Author
Uchenna Wisdom Chiziterem
Cybersecurity Student | Python Developer | SOC & Cloud Security Enthusiast | Aspiring Cybersecurity Architect
