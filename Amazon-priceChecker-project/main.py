import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from pprint import pprint
import os


URL = "https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Cosmic-5/dp/B094WN6SY2/" \
      "ref=sr_1_3?crid=J0IBA8SYEFJA&dchild=1&keywords=playstation+5&qid=1633482718&sprefix=plays%2Caps%2C162&sr=8-3"
USER_AGENT = os.environ.get("USER_AGENT")
ACCEPT_LANGUAGE = "en-us"

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

RECEIVING_EMAIL = os.getenv("RECEIVING_EMAIL")

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
html = response.text
# pprint(html)
soup = BeautifulSoup(html, "lxml")

price = soup.find(name="span", class_="priceBlockBuyingPriceString")

price_amount = float(price.text.split("$")[1])

if price_amount < 60.0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=RECEIVING_EMAIL, msg=f" Sale on new item!!!\n\n"
                                                                                  f" PlayStation DualSense "
                                                                                  f"Wireless Controller - Cosmic Red "
                                                                                  f"now ${str(price_amount)}.\n{URL}")

