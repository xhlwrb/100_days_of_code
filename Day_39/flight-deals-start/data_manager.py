import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/0cd8e40c14a33afcd27d438a81dd8f71/flightDeals2/prices"
        self.sheety_headers = {
            "Authorization": "Bearer flightdeals",
        }

    def get_row(self):
        get_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        get_response.raise_for_status()
        prices_value = get_response.json()["prices"]
        return prices_value

    def set_iata(self, sheet_data):
        for each_city in sheet_data:
            row_id = each_city["id"]
            set_endpoint = f"{self.sheety_endpoint}/{row_id}"
            sheety_config = {
                "price": {
                    "iataCode": each_city["iataCode"],
                }
            }
            set_response = requests.put(url=set_endpoint, json=sheety_config, headers=self.sheety_headers)

    def set_new_price(self, row_id, new_price):
        set_endpoint = f"{self.sheety_endpoint}/{row_id}"
        sheety_config = {
            "price": {
            "lowestPrice": new_price,
            }
        }
        set_response = requests.put(url=set_endpoint, json=sheety_config, headers=self.sheety_headers)
        set_response.raise_for_status()




