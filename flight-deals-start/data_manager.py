import requests
from pprint import pprint

PRICES_SHEETY_ENDPOINT = "https://api.sheety.co/1cf2ad8aee2c931b25f8106e770a68ed/flightDeals/prices"
USERS_SHEETY_ENDPOINT = "https://api.sheety.co/1cf2ad8aee2c931b25f8106e770a68ed/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=PRICES_SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{PRICES_SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = USERS_SHEETY_ENDPOINT

        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data