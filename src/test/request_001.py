import requests
import json

api_key = 'ded0add2b4cdc90d9a529ece52fa986b'

new_header = {'api-key': api_key}

url = "https://api.scripture.api.bible/v1/bibles"

response = requests.get(url, headers=new_header)

json_response = json.loads(response.text)

#print(json.dumps(json_response, indent=3))

assert json_response['data'][0]['id'] != None, "El campo esta vacio"
assert json_response['data'][0]['language']['nameLocal'] == 'Nend'

print (json_response['data'][0]['id'],json_response['data'][0]['language']['nameLocal'])