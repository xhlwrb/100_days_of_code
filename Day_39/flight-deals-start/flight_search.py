import requests
from flight_data import FlightData
from datetime import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = "LpsAAtZTGAw0jzDTDF5cexTzyiM1_Dkf"
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey": self.api_key,
        }

    def get_iata_code(self, city_name):
        location_config = {
            "term": city_name,
            "location_types": "city",
        }
        get_response = requests.get(url=self.location_endpoint, params=location_config, headers=self.headers)
        get_response.raise_for_status()
        return get_response.json()["locations"][0]["code"]

    def search_flight(self, from_city, to_city, date_from, date_to):
        search_config = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        get_response = requests.get(url=self.search_endpoint, params=search_config, headers=self.headers)
        get_response.raise_for_status()

        try:
            data = get_response.json()["data"][0]
        except IndexError:
            print(f"No flights for {to_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][0]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ￡{flight_data.price}")

        return flight_data


# flight_search = FlightSearch()
# flight_search.search_flight("PAR", "BER", datetime.today().strftime("%d/%m/%Y"), datetime.today().strftime("%d/%m/%Y"))
