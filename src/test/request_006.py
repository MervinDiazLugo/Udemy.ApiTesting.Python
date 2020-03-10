import requests

url = "https://gorest.co.in/public-api/users?_format=json&access-token=-cNWndrZ5D6r9vtqpaVNt7KVKegehsvnljUY"


response = requests.get(url)

print(response.text)