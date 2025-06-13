import requests
from math import sqrt
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time
from config import *

TO = "samuellywang@gmail.com"

def compare(time1, time2):
    fmt = '%H:%M:%S'
    t1 = datetime.strptime(time1, fmt)
    t2 = datetime.strptime(time2, fmt)
    return t1 < t2

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

def distance(position1, position2):
    return sqrt(
        (float(position1['latitude']) - float(position2['latitude'])) ** 2 +
        (float(position1['longitude']) - float(position2['longitude'])) ** 2
    )
location = requests.get('https://ipinfo.io').json()
# print(ISS_location)
cur_pos = {'latitude': location['loc'].split(',')[0],
           'longitude': location['loc'].split(',')[1]}
# print(f"You are currently {dist_mi:.2f} miles away from the ISS.")

# print(f"Sunrise at: {sunrise_time}, Sunset at: {sunset_time}, Current time: {current_time}, Is it dark? {'Yes' if is_dark else 'No'}")

while True:
    ISS_location = requests.get('http://api.open-notify.org/iss-now.json').json()
    iss_pos = {'latitude': ISS_location['iss_position']['latitude'],
           'longitude': ISS_location['iss_position']['longitude']}
    dist_deg=distance(cur_pos, iss_pos)
    dist_mi= dist_deg * 69  # Approximate conversion from degrees to miles
    #see if the sky is dark
    response = requests.get('https://api.sunrise-sunset.org/json', params={
        'lat': cur_pos['latitude'],
        'lng': cur_pos['longitude'],
        'formatted': 0,
        'tzid': 'America/New_York'  # Adjust timezone as needed
    }).json()
    time.sleep(60)
    sunrise = response['results']['sunrise']
    sunset = response['results']['sunset']
    sunrise_time = str(datetime.fromisoformat(sunrise))[11:19]
    sunset_time = str(datetime.fromisoformat(sunset))[11:19]
    current_time = str(datetime.now())[11:19]
    is_dark = compare(current_time, sunrise_time) or compare(sunset_time, current_time)
    if dist_mi < 100 and is_dark:
        SUBJECT = "Look up"
        BODY = "The ISS is currently overhead! You are within 100 miles of it.\n\n" \
                        "Check out the live feed at https://www.nasa.gov/nasalive\n\n"
        try:
            send_email(TO, SUBJECT, BODY)
        except Exception as e:
            print(f"Failed to send email to {TO}: {e}")