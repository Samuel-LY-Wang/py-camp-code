#sends a random email to all of my email addresses every morning with a quote and reminder to check calendar
#these emails should be whitelisted by my personal, umass, davidson, and lexington emails

import smtplib
from email.mime.text import MIMEText
import datetime
import random
# Email configuration
TO = [
    "samuellywang@gmail.com",
    "25stu478@lexingtonma.org",
    "samwang@umass.edu",
    "sawang@davidsononline.org",
    "wamsang1434@gmail.com",
    "pumac2024lexalpha@gmail.com"
]
with open("quotes.txt", "r") as f:
    quotes = f.readlines()
    if not quotes:
        raise ValueError("The quotes file is empty.")
def send_email(to_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM
    msg['To'] = to_address

    with smtplib.SMTP(SERVER, PORT) as server:
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, to_address, msg.as_string())
        print(f"Email sent to {to_address}")
cur_day = datetime.date.today()
while True:
    if cur_day != datetime.date.today() and datetime.datetime.now().hour == 9: #send all the emails at 9 AM
        cur_day = datetime.date.today()
        for recipient in TO:
            SUBJECT = "A new day, a new email"
            BODY = f"Today is {datetime.datetime.now().strftime("%Y-%m-%d")}. Don't forget to check your calendar!\n\nToday's quote is:\n{random.choice(quotes).strip()}\n\nHave a great day!"
            try:
                send_email(recipient, SUBJECT, BODY)
            except Exception as e:
                print(f"Failed to send email to {recipient}: {e}")