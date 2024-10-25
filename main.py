import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    
    "token": "token",
    "username": "elalovesporsche",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

USERNAME= "elalovesporsche"
TOKEN = "token"
#esponse = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Reading Book Graph",
    "unit":"commit",
    "type":"int",
    "color":"momiji",
}

headers = {
    "X-USER-TOKEN":TOKEN
}

GRAPH_ID = "graph1"
#response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=10, day=25)


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"1"
    
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"3",
}

#response = requests.put(url=update_endpoint,json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)
