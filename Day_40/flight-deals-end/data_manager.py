from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0cd8e40c14a33afcd27d438a81dd8f71/flightDeals2/prices"
SHEETY_SHEET2_ENDPOINT = "https://api.sheety.co/0cd8e40c14a33afcd27d438a81dd8f71/flightDeals2/sheet2"
SHEETY_HEADERS = {
            "Authorization": "Bearer flightdeals",
}

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_data(self):
        response = requests.get(url=SHEETY_SHEET2_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.customer_data = data["sheet2"]
        return self.customer_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS,
            )
            print(response.text)
