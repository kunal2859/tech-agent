import smtplib
import os

def send_email(articles):
    if not articles:
        print("No relevant articles found.")
        return

    sender = os.getenv("EMAIL")
    password = os.getenv("APP_PASSWORD")
    receiver = sender

    subject = "🚀 New Tech Launch Updates"

    body = ""

    for article in articles:
        body += f"""
Title: {article['title']}
Link: {article['link']}
-----------------------------------
"""

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)