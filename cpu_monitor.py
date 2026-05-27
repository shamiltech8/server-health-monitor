import psutil
import time
import subprocess
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

log_file = f"logs/health_{timestamp}.log"

def log_message(message):
    print(message)
    with open(log_file,"a") as file:
        file.write(message +"\n")

log_message(f"\n===== SYSTEM REPORT {datetime.now()} =====")

log_message("SYSTEM MONITOR")

cpu_usage = psutil.cpu_percent(interval=1)

log_message(f"CPU USAGE:{cpu_usage}%")

if cpu_usage > 80:
    log_message("WARNING: High cpu usage") 
else:
    log_message("cpu usage is normal")


memory = psutil.virtual_memory()

memory_usage = memory.percent
 
log_message(f"MEMORY USAGE :{memory_usage}%")

if memory_usage >  80:
    log_message("WARNING: High Memory Usage")
else:
    log_message("Normal Memory Usage")


disk = psutil.disk_usage('/')
 
disk_usage = disk.percent

log_message(f"DISK USAGE:{disk_usage}%")

if disk_usage > 80:
    log_message("WARNING: High Disk Usage")
else: 
    log_message("Normal Disk Usage")


boot_time = psutil.boot_time()

current_time = time.time()
 
uptime_secounds = current_time-boot_time

uptime_hours = uptime_secounds // 3600

log_message(f"System Uptime: {uptime_hours}Hours")


services = ["cron","ssh","NetworkManager"]
 
log_message("\nSERVICE CHECK")

for service in services:
    result = subprocess.run(
        ["systemctl","is-active","--quiet",service]
 
    )

    if result.returncode == 0:
        log_message(f"{service} service is running")
    else:
        log_message(f"WARNING: {service} service is Down")
