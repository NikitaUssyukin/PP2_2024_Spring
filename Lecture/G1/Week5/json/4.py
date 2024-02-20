import json

file = open("car.json")

car_json = file.read()

car = json.loads(car_json)

car["year"] = 2011
car["num_of_crashes"] = 0
car["owner"] = "Anya"

car_json = json.dumps(car, indent=4)

file = open("car_edited.json", "w")

file.write(car_json)

print(car)