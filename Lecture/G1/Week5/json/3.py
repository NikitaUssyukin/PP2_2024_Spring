import json

file = open("car.json")

car_json = file.read()

car = json.loads(car_json)

print(car)