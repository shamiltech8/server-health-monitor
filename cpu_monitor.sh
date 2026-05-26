#!/bin/bash

echo ""
echo "CPU USAGE"

top -bn1 | grep "Cpu"

echo ""
echo "CPU ALERT"

CPU_INT=$(mpstat 1 1 | awk '/Average/ {printf "%.0f", 100 - $NF}')

if [ "$CPU_INT" -gt 80 ]
then
    echo "WARNING: High CPU Usage - $CPU_INT%"
else
    echo "CPU Usage is Normal - $CPU_INT%"
fi
