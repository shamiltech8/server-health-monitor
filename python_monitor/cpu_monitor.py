import psutil

def cpu_check():

    print("\nCPU MONITOR")

    cpu_usage = psutil.cpu_percent(interval=1)

    print(f"CPU Usage: {cpu_usage}%")

    if cpu_usage > 80:
        print("WARNING: High CPU Usage")
    else:
        print("CPU Usage is Normal")



