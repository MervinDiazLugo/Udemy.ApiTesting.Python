import requests
import json

header = {"Content-Type":"application/json", "Authorization": "Bearer " + "AAAAAAAAAAAAAAAAAAAAJG2CQEAAAAAiyUNrX2he%2FCbTte5YGN6e8ernYo%3D0z7XZJCkEUydWO4qeT7qUN11dKCHpQMwHfMnQQLEo3HhNEPJcG"}

tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'

tweet_response = requests.get(tweet, headers = header)

_response = json.loads(tweet_response.text)

print(json.dumps(_response, indent=3))