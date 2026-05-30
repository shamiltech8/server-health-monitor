import subprocess

def service_check():

    services = ["cron", "ssh", "NetworkManager"]

    print("\nSERVICE CHECK")

    for service in services:

        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service]
        )

        if result.returncode == 0:
            print(f"{service} service is running")
        else:
            print(f"WARNING: {service} service is DOWN")
