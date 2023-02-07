import requests
import os
from datetime import datetime

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
GENDER = "female"
WEIGHT_KG = 55
HEIGHT_CM = 165
AGE = 28
today = datetime.today()

input_sentence = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": input_sentence,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=exercise_headers)
response.raise_for_status()
result = response.json()

sheety_headers = {
    "Authorization": BEARER_TOKEN,
}

for exercise in result["exercises"]:
    sheety_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(sheety_headers)

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_headers)
    # response.raise_for_status()
    print(response)
    print(response.text)
