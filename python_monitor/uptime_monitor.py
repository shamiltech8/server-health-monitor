import psutil
import time
from logger import write_log

def uptime_check():

    print("\nUPTIME MONITOR")

    boot_time = psutil.boot_time()

    current_time = time.time()

    uptime_seconds = current_time - boot_time

    uptime_hours = round(uptime_seconds / 3600, 2)

    print(f"System Uptime: {uptime_hours} Hours")
    write_log(f"System Uptime: {uptime_hours} Hours")


    return uptime_hours


