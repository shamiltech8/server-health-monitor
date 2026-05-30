import psutil

def disk_check():

    print("\nDISK MONITOR")

    disk = psutil.disk_usage('/')

    disk_usage = disk.percent

    print(f"Disk Usage: {disk_usage}%")

    if disk_usage > 80:
        print("WARNING: High Disk Usage")
    else:
        print("Disk Usage is Normal")
