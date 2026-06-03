import subprocess
from logger import write_log
from email_alert import send_email_alert
def service_check():

    services = ["cron", "ssh", "NetworkManager"]

    print("\nSERVICE CHECK")

    for service in services:

        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service]
        )

        if result.returncode == 0:
            print(f"{service} service is running")
            write_log(f"{service} service is running")
        else:
            print(f"WARNING: {service} service is DOWN")
            write_log(f"WARNING: {service} service is DOWN")
 
            send_email_alert(
                "SERVICE ALERT",
                f"{service} Service is Down"
            )
