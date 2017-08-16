import json
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
ex = json.loads(example)
print(ex.keys())
print(ex['weather'])
print(ex['weather'][0])
print(ex['weather'][0]['description'])
# documentation https://openweathermap.org/current
# our final dictionary
# keys are temp, humidity, wind_speed, wind_direction, percent_clouds
# how to access the information similar to print stateents
# store data in individual variables
percent_clouds = ex['clouds']['all'] # should be 92
print(92)
# do that for all the keys
# then put in dictionary
weather_dictionary = {'Cloudiness':percent_clouds} # separate each Key:value with a comma
sample_dictionary = {'1':'a', '2': 'b'}
