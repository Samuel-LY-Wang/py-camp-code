import requests
import geocoder
import smtplib
from email.mime.text import MIMEText
from dotenv import dotenv_values

g=geocoder.ip('me')
[lat,lon]=g.latlng

EMAIL_EXT="mms.cricketwireless.net"

config=dotenv_values(".env")

def send_email(to_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config["FROM"]
    msg['To'] = to_address

    with smtplib.SMTP(config["SERVER"], config["PORT"]) as server:
        server.starttls()
        server.login(config["FROM"], config["PASS"])
        server.sendmail(config["FROM"], to_address, msg.as_string())
        print(f"Email sent to {to_address}")

#I tried very hard to make texting work, but I just couldn't
#Twilio seemed to have much stricter regulations and texting via email was going to lose support in 4 days anyways
def text(message):
    global TO
    SUBJECT="Update on today's weather"
    BODY=message
    try:
        send_email(TO,SUBJECT,BODY)
    except Exception as e:
        print(f"Failed to send email to {TO}: {e}")

weather = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=5&appid={WEATHER_API_KEY}').json()['list']

for forecast in weather:
    t=(int(forecast['dt_txt'][-8:-6])-4)%24
    # print(t)
    conditions = forecast['weather']
    notify = ""
    temp=(forecast['main']['temp']-273)*1.8+32 # temp in F
    if temp >= 75:
        notify = notify+f"It will be rather hot at {t}:00. Bring lots of water!\n"
    elif temp >= 65:
        pass
    elif temp >= 55:
        notify = notify+f"Bit chilly at {t}:00. Wear long sleeves!\n"
    elif temp >= 40:
        notify = notify+f"Quite cold at {t}:00. Remember to wear your jacket!\n"
    else:
        notify = notify+f"It will be very cold at {t}:00! Dress warmly and avoid being outside for too long!\n"
    for condition in conditions:
        actual_condition = condition['id']
        if 200<=actual_condition<=300:
            notify = notify+f"Watch out! There will be a thunderstorm today at {t}:00! Bring an umbrella!\n"
        elif actual_condition <= 600:
            notify = notify+f"It will rain today at {t}:00. Bring an umbrella!\n"
        elif actual_condition <= 700:
            notify = notify+f"It is going to snow today at {t}:00\n"
if len(notify) > 0:
    text(notify)
else:
    text("All good today!")