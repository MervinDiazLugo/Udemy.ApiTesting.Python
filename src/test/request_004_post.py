import requests
import json

url = f"https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json", "accept": "application/json"}
body = """{
  "id": 500,
  "category": {
    "id": 3,
    "name": "Mutantes"
  },
  "name": "Wolverine",
  "photoUrls": [
    "url1",
    "url2"
  ],
  "tags": [
    {
      "id": 1,
      "name": "XXX"
    },
    {
      "id": 2,
      "name": "Garras de adamantium"
    }
  ],
  "status": "available"
}"""
response = requests.post(url, headers = headers, data=body)


json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))

