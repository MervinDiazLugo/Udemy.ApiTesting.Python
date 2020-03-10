import requests
import json

api_key = "QlyoXK3iIUw5Nm3W8Bgsanqys"

api_secret = "kAm5eRDyMWqZ3SAJA90IvFjFgfwL2BRWAIY15nI4JWHxBQeMl3"

url = "https://api.twitter.com/oauth2/token"

body = {"grant_type":"client_credentials"}

response = requests.post(url, auth=(api_key, api_secret), data=body)

Autorization_response = json.loads(response.text)

print(json.dumps(Autorization_response, indent=3))


header = {"Content-Type":"application/json", "Authorization": "Bearer " + Autorization_response['access_token']}

tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'

tweet_response = requests.get(tweet, headers = header)

_response = json.loads(tweet_response.text)

print(json.dumps(_response, indent=3))