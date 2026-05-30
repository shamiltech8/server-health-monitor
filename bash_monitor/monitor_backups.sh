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
