#!/bin/bash

LOG_FILE="logs/health.log"

mkdir -p logs

{
echo "============================"
echo "SERVER HEALTH MONITOR"
echo "============================"

echo ""
echo "DATE & TIME"
date

echo ""
echo "CPU USAGE"
top -bn1 | grep "Cpu"

echo ""
echo "MEMORY USAGE"
free -h

echo ""
echo "DISK USAGE"
df -h

echo ""
echo "SYSTEM UPTIME"
uptime

echo ""
echo "TOP 5 PROCESSES"
ps aux --sort=-%mem | head -n 6

echo ""
echo "============================"

} >> "$LOG_FILE"

echo "Health report saved to $LOG_FILE"
#!/bin/bash

mkdir -p /home/user/server_health_monitor/logs

LOGFILE="/home/user/server_health_monitor/logs/health_$(date +%Y-%m-%d_%H-%M-%S).log"

echo "============================" | tee -a $LOGFILE
echo "SERVER HEALTH MONITOR" | tee -a $LOGFILE
echo "============================" | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "DATE & TIME" | tee -a $LOGFILE
date | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "CPU USAGE" | tee -a $LOGFILE
top -bn1 | grep "Cpu" | tee -a $LOGFILE

echo "" | tee  -a $LOGFILE
echo "CPU USAGE ALERT" | tee -a $LOGFILE

CPU_INT=$(mpstat 1 1 | awk '/Average/ {printf "%.0f", 100 - $12}')


CPU_INT=${CPU_INT%.*}

if [ "$CPU_INT" -gt 80 ]
then
    echo "WARNING: High CPU Usage - $CPU_INT%" | tee -a $LOGFILE
    echo "WARNING: High CPU Usage - $CPU_INT%" | mail -s "SERVER ALERT" shamil6282669@gmail.com
else
    echo "CPU Usage is Normal - $CPU_INT%" | tee -a $LOGFILE
fi

echo "" | tee -a $LOGFILE
echo "MEMORY ALERT" | tee -a $LOGFILE

MEMORY_USAGE=$(free | awk '/Mem:/ {printf "%.0f", $3/$2 * 100}')

if [ "$MEMORY_USAGE" -gt 80 ]
then
    echo "WARNING: High Memory Usage - $MEMORY_USAGE%" | tee -a $LOGFILE
    echo "WARNING: High Memory Usage - $MEMORY_USAGE%" | mail -s "MEMORY ALERT" shamil6282669@gmail.com
else
    echo "Memory Usage is Normal - $MEMORY_USAGE%" | tee -a $LOGFILE
fi

echo "" | tee -a $LOGFILE
echo "SERVICE CHECK" | tee -a $LOGFILE

SERVICES=("cron" "ssh" "NetworkManager")

for  SERVICE in "${SERVICES[@]}"
do

if systemctl is-active --quiet "$SERVICE"
then
        echo "$SERVICE service is running" | tee -a $LOGFILE
    else
        echo "WARNING: $SERVICE service is DOWN" | tee -a $LOGFILE
        echo "WARNING: $SERVICE service is DOWN" | mail -s "SERVICE ALERT" shamil6282669@gmail.com
    fi
done

echo "" | tee -a $LOGFILE
echo "MEMORY USAGE" | tee -a $LOGFILE
free -h | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "DISK USAGE" | tee -a $LOGFILE
df -h | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "SYSTEM UPTIME" | tee -a $LOGFILE
uptime | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "TOP 5 PROCESSES" | tee -a $LOGFILE
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -6 | tee -a $LOGFILE

echo "" | tee -a $LOGFILE
echo "INTERNET CHECK" | tee -a $LOGFILE

ping -c 1 google.com > /dev/null 2>&1

if [ $? -eq 0 ]
then
    echo "Internet is Connected" | tee -a $LOGFILE
else
    echo "Internet is NOT Connected" | tee -a $LOGFILE
fi

echo "" | tee -a $LOGFILE
echo "DISK WARNING CHECK" | tee -a $LOGFILE

DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ $DISK_USAGE -gt 80 ]
then
    echo "WARNING: Disk usage is above 80%" | tee -a $LOGFILE
else
    echo "Disk usage is under control" | tee -a $LOGFILE
fi

echo "" | tee -a $LOGFILE
echo "============================" | tee -a $LOGFILE

echo "Health report saved to $LOGFILE"

find /home/user/server_health_monitor/logs/ -type f -mmin +1  -delete


