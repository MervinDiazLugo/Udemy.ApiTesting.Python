import requests
import datetime
import json

Format = "%Y-%m-%d"
BackDay = datetime.date.today() - datetime.timedelta(days=2)
Day = BackDay.strftime(Format)


api_key = 'VAQkYOYJlDKaa7PZYHMnq79kbP5MrGS5FxqAhuwX'

date = str(datetime.date.today().strftime("%Y-%m-%d"))

hd = 'False'

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={Day}&hd={hd}"

response = requests.request("GET", url)

print(response.text)

response.status_code == 200

