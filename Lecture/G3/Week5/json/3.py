import json

file = open("car.json")

car_json = file.read()

car = json.loads(car_json)

key = input()
print(car[key])