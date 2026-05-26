#!/bin/bash

echo ""
echo "SERVICE CHECK"

SERVICES=("cron" "ssh" "NetworkManager")

for SERVICE in "${SERVICES[@]}"
do
    if systemctl is-active --quiet "$SERVICE"
    then
        echo "$SERVICE service is running"
    else
        echo "WARNING: $SERVICE service is DOWN"
    fi
done
