import subprocess
from logger import write_log
from email_alert import send_email_alert

def service_check():

    service_names = ["cron", "ssh", "NetworkManager"]

    services = {}

    print("\nSERVICE CHECK")

    for service in service_names:

        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service]
        )

        if result.returncode == 0:
            print(f"{service} service is running")
            write_log(f"{service} service is running")

            services[service] = "Running"

        else:
            print(f"WARNING: {service} service is DOWN")
            write_log(f"WARNING: {service} service is DOWN")

            services[service] = "DOWN"

            send_email_alert(
                "SERVICE ALERT",
                f"{service} Service is Down"
            )

    return services
