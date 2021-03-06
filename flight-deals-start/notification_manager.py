import os

import requests
from twilio.rest import Client
import smtplib
from flight_data import FlightData
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN=")
TWILIO_NUMBER = "+16464900243"
RECEIVING_NUMBER = os.environ.get("RECEIVING_NUMBER")
MY_EMAIL = "pythonicpr@gmail.com"
MY_PASSWORD = os.environ.get("MY_PASSWORD")
class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self,message):

        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=RECEIVING_NUMBER
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
            )
