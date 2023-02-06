import requests
from datetime import datetime

APP_ID = "c6ae685c"
API_KEY = "6ea8112df3e7afbe4dfd9ebe24502eb4"
today = datetime.today()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

input_sentence = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": input_sentence,
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
response.raise_for_status()
print(response)

