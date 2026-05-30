import psutil

def memory_check():

    print("\nMEMORY MONITOR")

    memory = psutil.virtual_memory()

    memory_usage = memory.percent

    print(f"Memory Usage: {memory_usage}%")

    if memory_usage > 80:
        print("WARNING: High Memory Usage")
    else:
        print("Memory Usage is Normal")
