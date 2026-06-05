from datetime import datetime

def save_report(report_text):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = f"reports/report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(report_text)

    print(f"Report saved: {filename}")
