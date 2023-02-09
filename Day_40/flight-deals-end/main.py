from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_customer_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"


# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    if flight is None:
        print(f"There's no flights from London to {destination['city']}.")
        continue

    if flight.price < destination["lowestPrice"]:
        telegram_message = f"Low price alert! Only £{flight.price} to "\
                  f"fly from {flight.origin_city}-{flight.origin_airport} "\
                  f"to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}.\n"
        if flight.stop_overs > 0:
            telegram_message += f"This flight has 1 stop over, via {flight.via_city}."
        notification_manager.telegram_bot_sendtext(telegram_message)

        email_message = f"Subject:New Price Found!\n\n" \
                        f"Low price alert! " \
                        f"Only ￡{flight.price} to fly from " \
                        f"{flight.origin_city} to {flight.destination_city}, " \
                        f"from {flight.out_date} to {flight.return_date}.\n" \
                        f"https://www.google.co.uk/flights?hl=en#flt=" \
                        f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}" \
                        f"*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        email_message.encode('utf-8')
        notification_manager.send_emails(customer_data, email_message.encode('utf-8'))

