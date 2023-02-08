# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

import os
import requests
from datetime import datetime
from datetime import timedelta
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# TODO: add city code
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_row()
today = datetime.now()

# check if sheet_data contains any values for the iatacode key
for each_city in sheet_data:
    if each_city["iataCode"] == "":
        # pass city name to  flightsearch class & update sheet_data
        iata_code = flight_search.get_iata_code(each_city["city"])
        each_city["iataCode"] = iata_code

# print sheet_data
print("sheet_date after code", sheet_data)

# set iata code
# data_manager.set_iata(sheet_data)
print("after")

# TODO: use flight search API to check for the cheapest flights
#  from London to all destinations in sheety.(direct flights, tomorrow to 6 months later,
#  round trips return in 7-28 days, currency GBP)
from_city = "LON"
to_city = "BER"
today_date_str = today.date().strftime("%d/%m/%Y")
six_months_later = today + timedelta(days=180)
six_months_later_str = six_months_later.strftime("%d/%m/%Y")
# def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport,
#                  out_date, return_date):
flight_data = flight_search.search_flight(from_city, to_city, today_date_str, six_months_later_str)

# TODO: if lower than in google sheet, then send messages via telegram
# update price
for each_city in sheet_data:
    if each_city["city"] == flight_data.destination_city:
        if flight_data.price < each_city["lowestPrice"]:
            print(flight_data)
            data_manager.set_new_price(each_city["id"], flight_data.price)
            # send via telegram
            notification_manager = NotificationManager()
            t = "TEST"
            notification_manager.telegram_bot_sendtext(f"Low price alert! Only ￡{flight_data.price} "
                                                       f"to fly from "
                                                       f"London-{flight_data.origin_airport} "
                                                       f"to {flight_data.destination_city}"
                                                       f"-{flight_data.destination_airport}, "
                                                       f"from {flight_data.out_date} "
                                                       f"to {flight_data.return_date}.")