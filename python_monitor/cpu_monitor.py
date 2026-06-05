import psutil
from logger import  write_log
from email_alert import send_email_alert
from config_loader import get_config

def cpu_check():

    config = get_config()
    cpu_threshold = config["cpu_threshold"]

    print("\nCPU MONITOR")

    cpu_usage = psutil.cpu_percent(interval=1)

    print(f"CPU Usage: {cpu_usage}%")
    write_log(f"CPU Usage: {cpu_usage}%")

    if cpu_usage > cpu_threshold:
        print("WARNING: High CPU Usage")
        write_log("WARNING: High CPU Usage")

        send_email_alert(
            "CPU ALERT",
            f"CPU Usage is High: {cpu_usage}%"
        )
    else:
        print("CPU Usage is Normal")
        write_log("CPU Usage is Normal")


    return cpu_usage
