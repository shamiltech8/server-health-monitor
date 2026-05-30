#!/bin/bash

echo ""
echo "MEMORY ALERT"

MEMORY_USAGE=$(free | awk '/Mem:/ {printf "%.0f", $3/$2 * 100}')

if [ "$MEMORY_USAGE" -gt 80 ]
then
    echo "WARNING: High Memory Usage - $MEMORY_USAGE%"
else
    echo "Memory Usage is Normal - $MEMORY_USAGE%"
fi
