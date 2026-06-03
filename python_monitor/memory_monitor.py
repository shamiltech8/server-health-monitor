import psutil
from logger import write_log
from email_alert import send_email_alert
from config_loader import get_config

def memory_check():

    config = get_config()
    memory_threshold = config["memory_threshold"]

    print("\nMEMORY MONITOR")

    memory = psutil.virtual_memory()

    memory_usage = memory.percent

    print(f"Memory Usage: {memory_usage}%")
    write_log(f"Memory Usage: {memory_usage}%")

    if memory_usage > memory_threshold:
        print("WARNING: High Memory Usage")
        write_log("WARNING: High Memory Usage")

        send_email_alert(
            "MEMORY  ALERT",
            f"Memory Usage is High: {memory_usage}%"
        )
    else:
        print("Memory Usage is Normal")
        write_log("Memory Usage is Normal")
