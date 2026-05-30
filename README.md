# Server Health Monitor

A Linux-based Server Health Monitoring System developed using Bash and Python. This project monitors system resources, checks service status, generates logs, and automates basic server health management tasks.

## Features

### Bash Monitoring System
- CPU Usage Monitoring
- Memory Usage Monitoring
- Service Status Monitoring
- Disk Usage Monitoring
- Internet Connectivity Check
- System Uptime Monitoring
- Automatic Log Generation
- Automatic Old Log Cleanup

### Python Monitoring System
- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Service Monitoring
- System Uptime Monitoring
- Modular Monitoring Architecture
- Log Cleanup Module

## Project Structure

```text
server_health_monitor/
├── bash_monitor/
│   ├── monitor.sh
│   ├── cpu_monitor.sh
│   ├── memory_monitor.sh
│   ├── service_monitor.sh
│   ├── main_monitor.sh
│   └── monitor_backups.sh
├── python_monitor/
│   ├── main_monitor.py
│   ├── cpu_monitor.py
│   ├── memory_monitor.py
│   ├── disk_monitor.py
│   ├── uptime_monitor.py
│   ├── service_monitor.py
│   └── log_cleanup.py
├── logs/
├── README.md
└── .gitignore
```

## Technologies Used

- Linux
- Bash Scripting
- Python
- Git
- GitHub
- psutil

## Installation

Clone the repository:

```bash
git clone https://github.com/shamiltech8/server-health-monitor.git
cd server-health-monitor
```

Install Python dependency:

```bash
pip install psutil
```

## Running the Bash Version

```bash
cd bash_monitor
./monitor.sh
```

## Running the Python Version

```bash
cd python_monitor
python3 main_monitor.py
```

## Sample Checks Performed

- CPU Usage Threshold Monitoring
- Memory Usage Threshold Monitoring
- Disk Space Monitoring
- Service Health Verification
- System Uptime Reporting
- Log File Management

## Learning Outcomes

This project helped me learn:

- Linux Administration Basics
- Bash Scripting
- Python Scripting
- System Monitoring Concepts
- Service Management with systemctl
- Log Management
- Git and GitHub Workflow
- Modular Project Design

## Future Improvements

- Email Alert System
- CSV Report Export
- Configuration File Support
- Dashboard Integration
- Docker Deployment
- Web-Based Monitoring Interface

## Author

MUHAMMED SHAMIL KT

GitHub: https://github.com/shamiltech8
