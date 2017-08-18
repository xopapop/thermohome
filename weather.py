from classes import weather
import json
import requests
base_url = 'http://api.openweathermap.org/data/2.5/weather?zip=43201,us&appid='
key_file = open('api_keys.txt','r')
key = key_file.readline()
key_file.close()
api_url = base_url+key
api_response = requests.get(api_url)
print(api_response.text)
example = """{"coord":{"lon":139,"lat":35},
"sys":{"country":"JP","sunrise":1369769524,"sunset":1369821049},
"weather":[{"id":804,"main":"clouds","description":"overcast clouds","icon":"04n"}],
"main":{"temp":289.5,"humidity":89,"pressure":1013,"temp_min":287.04,"temp_max":292.04},
"wind":{"speed":7.31,"deg":187.002},
"rain":{"3h":0},
"clouds":{"all":92},
"dt":1369824698,
"id":1851632,
"name":"Shuzenji",
"cod":200}"""
#documentation: openweathermap.org/current
#variables
ex = json.loads(api_response.text)
dt = ex['dt']
temp_k = ex['main']['temp']
rh = ex['main']['humidity']
description = ex['weather'][0]['description']
wind_speed = ex['wind']['speed']
wind_angle = ex['wind']['deg']
#dictionary
weather_dict = {'dt':dt, 'temp_k':temp_k, 'rh':rh, 'description':description, 'wind_speed':wind_speed, 'wind_directions':wind_angle}
weather_obj = weather(weather_dict)