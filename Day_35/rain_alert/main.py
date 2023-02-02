import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
my_lat = 47.391930
my_long = 13.687420

weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


def telegram_bot_sendtext(bot_message):
    bot_token = "6093731261:AAH_sXfvkElXekEfEfttw-w7h3rp93Rw1t4"
    bot_chatID = "5738351415"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    test = telegram_bot_sendtext("bring umbrella")
    print(test)


