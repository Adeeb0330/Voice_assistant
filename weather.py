import requests

from News import json_data
from apikey import *

Api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid='+Api_key
json_data = requests.get(Api_address).json()

def temp():
    temperature = round(json_data['main']['temp']-275)
    return temperature

def des():
    description = json_data['weather'][0]['description']
    return description

print(temp())
print(des())