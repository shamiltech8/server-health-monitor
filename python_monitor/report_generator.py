from report_writer import save_report

def generate_report(
    cpu,
    memory,
    disk,
    uptime,
    services
):


    service_report = ""

    for service in services:

        service_report += (
            service + " : " +
            services[service] + "\n"
        )


    report = f"""

===== HEALTH REPORT =====

CPU Usage     : {cpu}%
Memory Usage  : {memory}%
Disk Usage    : {disk}%
Uptime        : {uptime} Hours


Services:
{service_report}
"""
    print(report)

    save_report(report)
