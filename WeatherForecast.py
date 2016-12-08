import json
import requests

city = "Stockholm"

appkey = "29b52869898fea9714d571d586e68840"

cityid = "524901"

getstringcurrent = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + appkey + "&units=metric"


r = requests.get(getstringcurrent)


print(r.json())




