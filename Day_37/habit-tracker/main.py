import requests
from datetime import datetime

USERNAME = "kathrynr"
TOKEN = "dpsjc9jda9wdjpa"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
print(today)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config['date']}"

update_config = {
    "quantity": "20",
}

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config['date']}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
