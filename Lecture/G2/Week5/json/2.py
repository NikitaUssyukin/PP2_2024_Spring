# JSON - JavaScript Object Notation
import json

car_json = '{"make": "Toyota", "color": "White", "year": 2023}'

car = json.loads(car_json)

key = input()
print(car[key])


