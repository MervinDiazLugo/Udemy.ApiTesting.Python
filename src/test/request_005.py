import requests
import json

url = f"https://api.twitter.com/labs/1/users?usernames=TwitterDev&format=detailed"

Auth = """OAuth oauth_consumer_key="QlyoXK3iIUw5Nm3W8Bgsanqys",oauth_token="1164675911049994240-rYR9Y7Ekq6WVUWTTN4CyymAeLRBq3n",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1582898113",oauth_nonce="rs2RqXGkHTW",oauth_version="1.0",oauth_signature="kgNhtbBCfNu%2FbLsLpy8a1Smaorg%3D"""

headers = {"Content-Type": "application/json", "accept": "application/json", "Authorization": Auth}

response = requests.get(url, headers = headers)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))
