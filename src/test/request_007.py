import requests

url = "https://gorest.co.in/public-api/users"

header = {"Content-Type":"application/json", "Authorization": "Bearer sr5Zoe13FCAa57iyF3x2twTYV2nHTLG6Dm1H"}

body = """{"first_name":"Mervin","last_name":"Diaz","gender":"male","email":"mervin100@hola.com","status":"active"}"""

response = requests.post(url, data=body, headers=header)

url = "https://gorest.co.in/public-api/users"
response = requests.get(url, headers=header)

print(response.text)