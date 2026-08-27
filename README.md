# 🛡️ Threat-Watch

> A Python-based Security Operations Center (SOC) simulation that analyzes authentication logs, detects brute-force attacks, classifies security events, and generates structured incident reports.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview
Threat-Watch is a Python-based SOC simulation designed to automate authentication log analysis and identify suspicious activity through threat classification and incident reporting.
This project reflects the workflow of a Security Operations Center by automating log analysis and highlighting suspicious authentication activity.

---

## ✨ Key Features

- 🔍 Parse authentication log files
- 📊 Display log events in a readable format
- 🚨 Detect repeated failed login attempts
- 🌐 Identify suspicious IP addresses
- ⚠️ Classify threats by severity
- 📄 Generate TXT incident reports
- 📦 Export reports to JSON
- 💻 Interactive Command-Line Interface (CLI)
- 🛠 Built-in exception handling

---

# 🏗️ Development Timeline

## Sprint 1 — Log Parsing

- Created sample authentication logs
- Parsed log entries into Python dictionaries
- Displayed parsed events

---

## Sprint 2 — Threat Detection

- Counted failed login attempts
- Identified suspicious IP addresses
- Generated brute-force alerts

---

## Sprint 3 — Threat Intelligence

- Implemented threat severity classification
- Improved alert formatting
- Added detection summaries

---

## Sprint 4 — Report Generation

- Generated TXT reports
- Exported detected threats
- Added report summaries

---

## Sprint 5 — Interactive CLI

- Built a menu-driven interface
- Added options for log analysis and reporting

---

## Sprint 6 — JSON Export

- Stored detections using dictionaries
- Exported structured JSON reports

---

## Sprint 7 — Error Handling

- Added exception handling
- Improved stability
- Displayed meaningful error messages


## Sprint 8 - AWS CloudTrail Integration
- Added log data from AWS CloudTrail to TreatWatch
- Cleaned log data, checked for missing values
- Counted events occured per Hour                                                                                         


---

# 📂 Project Structure

```text
Threat-Watch/
│
├── logs/
│   └── sample.log
│
├── reports/
│   ├── threat_report.txt
│   └── threat_report.json
│
├── screenshots/
│
├── src/
│   ├── parser.py
│   ├── detection.py
│   └── pydroid1.py
│
├── README.md
└── main.py
```

---

# 🛠 Technologies

- Python
- JSON
- Dictionaries
- Lists
- Functions
- Exception Handling
- File Handling

---

# 📈 Current Capabilities

✔ Log Parsing

✔ Threat Detection

✔ Threat Classification

✔ TXT Report Generation

✔ JSON Report Export

✔ Interactive CLI

✔ Error Handling

---

# 🚀 Planned Features

- [ ] AWS CloudTrail Integration
- [ ] Amazon S3 Support
- [ ] IAM Activity Monitoring
- [ ] Email Alerting
- [ ] Web Dashboard
- [ ] CSV Report Export
- [ ] Multiple Attack Detection
- [ ] Configurable Detection Thresholds

---

# 🎯 Learning Objectives

This project was created to strengthen practical skills in:

- Security Operations (SOC)
- Python Automation
- Log Analysis
- Threat Detection
- Incident Reporting
- Security Monitoring

---

# 👨‍💻 Author

**Uchenna Wisdom Chiziterem**

Cybersecurity Student | Python Developer | SOC & Cloud Security Enthusiast

**Goal:** Building practical cybersecurity projects while preparing for a career as a Cybersecurity Architect.

---

⭐ If you found this project interesting, consider giving it a star!
