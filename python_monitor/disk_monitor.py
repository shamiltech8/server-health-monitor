import psutil
from logger import write_log
from email_alert import send_email_alert
from config_loader import get_config

def disk_check():
 
    config = get_config()
    disk_threshold = config["disk_threshold"]

    print("\nDISK MONITOR")

    disk = psutil.disk_usage('/')

    disk_usage = disk.percent

    print(f"Disk Usage: {disk_usage}%")
    write_log(f"Disk Usage: {disk_usage}%")
    if disk_usage > disk_threshold:
        print("WARNING: High Disk Usage")
        write_log("WARNING: High Disk Usage")
       
        send_email_alert(
            "DISK ALERT",
            f"Disk Usage is High: {disk_usage}%"
        )
    else:
        print("Disk Usage is Normal")
        write_log("Disk Usage is Normal")
