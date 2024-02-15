import json

car_json = '{"make": "Subaru", "model": "Impreza", "year": 1995}'

car = json.loads(car_json)

key = input()
print(car[key])