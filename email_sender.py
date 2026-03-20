import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(articles):
    sender = os.getenv("EMAIL")
    password = os.getenv("APP_PASSWORD")
    receiver = sender

    subject = "🚀 New Tech Launch Updates"

    if not articles:
        body = "No relevant updates found."
    else:
        body = ""
        for article in articles:
            body += f"""
Title: {article['title']}
Link: {article['link']}
-------------------------
"""

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))  # 👈 IMPORTANT

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)  # 👈 use this instead of sendmail
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)