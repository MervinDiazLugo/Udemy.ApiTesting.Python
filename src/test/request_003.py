import requests
import json
import time

url = f"https://petstore.swagger.io/v2/pet/10"

response = requests.get(url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))

time.sleep(1)

assert json_response['id'] == 10, "No coincide"
assert json_response['name'] == 'Bod Conejito', "No coincide"
assert json_response['status'] == 'available', "No coincide"
assert json_response['photoUrls'][0] == 'https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg', "No coincide"
assert json_response['photoUrls'][1] == 'url2', "No coincide"
assert json_response['category']['id'] == 3
assert json_response['category']['name'] == 'Rabbits'