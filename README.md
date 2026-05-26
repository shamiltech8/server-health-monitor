# Server Health Monitor

A Linux-based server monitoring and alerting system built using Bash scripting.

## Features

- CPU monitoring
- Memory monitoring
- Disk usage monitoring
- Service monitoring
- Internet connectivity check
- Automatic log generation
- Alert system
- Email notifications
- Cron automation
- Multi-script architecture

## Technologies Used

- Linux
- Bash scripting
- Cron
- Mailutils
- Systemctl
- Mpstat

## Project Structure

```text
server_health_monitor/
├── cpu_monitor.sh
├── memory_monitor.sh
├── service_monitor.sh
├── main_monitor.sh
├── logs/
└── README.md
```

## How To Run

Make scripts executable:

```bash
chmod +x *.sh
```

Run monitoring system:

```bash
./main_monitor.sh
```

## Sample Features

### CPU Monitoring

Checks CPU usage and triggers alerts when usage exceeds threshold.

### Memory Monitoring

Calculates memory usage percentage and generates warnings.

### Service Monitoring

Checks important services like:
- cron
- ssh
- NetworkManager

### Logging System

Stores monitoring reports inside:
```text
logs/
```

### Email Alerts

Automatically sends email notifications for:
- High CPU usage
- High memory usage
- Service failures

## Skills Learned

- Linux administration
- Bash scripting
- Automation
- Monitoring systems
- Logging
- Debugging
- Cron jobs
- Modular scripting
- Git/GitHub workflow

## Future Improvements

- Python monitoring version
- Docker containerization
- Web dashboard
- Database logging
- Real-time monitoring
- Grafana integration

## Author

MUHAMMED SHAMIL KT
