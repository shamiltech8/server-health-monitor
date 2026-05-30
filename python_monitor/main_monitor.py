from cpu_monitor import cpu_check
from memory_monitor import memory_check
from disk_monitor import disk_check
from uptime_monitor import uptime_check
from service_monitor import service_check


print("SYSTEM MONITOR")


cpu_check()

memory_check()

disk_check()

uptime_check()

service_check()
