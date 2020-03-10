import requests
import json

url = f"https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json", "accept": "application/json"}
body = """{
  "id": 10,
  "category": {
    "id": 3,
    "name": "Rabbits"
  },
  "name": "Bod Conejito",
  "photoUrls": [
    "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg",
    "url2"
  ],
  "tags": [
    {
      "id": 1,
      "name": "tag3"
    },
    {
      "id": 2,
      "name": "tag4"
    }
  ],
  "status": "available"
}"""
response = requests.put(url, headers = headers, data=body)


json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))

assert json_response['id'] != None, "Esta Vacio"
