import os
import time
import requests
from InternetSpeedTwitterBot import InternetSpeedTwitterBot
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("USERNAME")
TWITTER_PW = os.getenv("PASSWORD")

bot = InternetSpeedTwitterBot(down=PROMISED_DOWN, up=PROMISED_UP)

print(bot.get_internet_speed())
