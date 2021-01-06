import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "bellaandsnowball"
TOKEN = "randomToken123"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# creating a user below
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Creating a graph below
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Meditation Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)