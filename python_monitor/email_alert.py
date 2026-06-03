import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(subject, message):

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv( "EMAIL_PASSWORD")


    email_body = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(sender_email,app_password)

    server.sendmail(
        sender_email,
        sender_email,
        email_body
    )

    server.quit()

    print("Email Alert Sent Succsessfully")
