'''
Este código foi escrito para acessar uma API REST via HTTP POST
'''


import json
import requests

url = "https://gpvsn123ya.execute-api.us-east-1.amazonaws.com/Post"
x = {
  "from": "Daniel",
  "to": "Ernest",
  "msg": "Heloooo Ernest!!!!!!!"
}
data_json = json.dumps(x)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
