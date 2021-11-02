import json
import requests

url = "https://gpvsn123ya.execute-api.us-east-1.amazonaws.com/Post"
x = {
  "from": "Rodrigo",
  "to": "Davi",
  "msg": "Perfeito"
}
data_json = json.dumps(x)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
