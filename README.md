# Server Health Monitor

A Linux-based Server Health Monitoring System developed using Bash and Python. The project monitors system resources, checks service status, generates reports, sends email alerts, performs log cleanup, and supports Docker-based deployment.

## Features

### Bash Monitoring System

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* Service Status Monitoring
* Internet Connectivity Check
* System Uptime Monitoring
* Automatic Log Generation
* Automatic Log Cleanup

### Python Monitoring System

* CPU Monitoring
* Memory Monitoring
* Disk Monitoring
* Uptime Monitoring
* Service Monitoring
* Email Alert System
* Health Report Generation
* Report Saving
* Automatic Log Cleanup
* JSON Configuration Support
* Docker Support
* Modular Architecture

## Technologies Used

* Linux
* Bash
* Python
* Docker
* Git
* GitHub
* psutil
* python-dotenv
* JSON

## Project Structure

```text
server_health_monitor/
├── bash_monitor/
│   ├── monitor.sh
│   ├── main_monitor.sh
│   ├── cpu_monitor.sh
│   ├── memory_monitor.sh
│   ├── service_monitor.sh
│   └── monitor_backups.sh
│
├── logs/
│
├── python_monitor/
│   ├── main_monitor.py
│   ├── cpu_monitor.py
│   ├── memory_monitor.py
│   ├── disk_monitor.py
│   ├── uptime_monitor.py
│   ├── service_monitor.py
│   ├── email_alert.py
│   ├── logger.py
│   ├── log_cleanup.py
│   ├── report_generator.py
│   ├── report_writer.py
│   ├── config_loader.py
│   ├── config.json
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── run_monitor.sh
│   ├── reports/
│   └── __pycache__/
│
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shamiltech8/server-health-monitor.git
cd server-health-monitor
```

Install dependencies:

```bash
cd python_monitor

pip install -r requirements.txt
```

## Running the Python Version

```bash
cd python_monitor

python3 main_monitor.py
```

## Docker Usage

Build the Docker image:

```bash
sudo docker build -t server-health-monitor .
```

Run the container:

```bash
sudo docker run server-health-monitor
```

## Sample Monitoring Output

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* Service Health Monitoring
* Uptime Tracking
* Email Notifications
* Log Management
* Health Report Generation

## Learning Outcomes

This project helped me learn:

* Linux Administration
* Bash Scripting
* Python Automation
* System Monitoring
* Service Management
* Log Management
* Email Automation
* JSON Configuration Management
* Docker Containerization
* Git and GitHub Workflow
* Modular Software Design

## Future Improvements

* Web Dashboard
* Database Integration
* Docker Compose
* Cloud Deployment
* Prometheus Integration
* Grafana Dashboard
* Kubernetes Deployment

## Author

MUHAMMED SHAMIL KT

GitHub: https://github.com/shamiltech8
