# JSON - JavaScript Object Notation
import json

car = {
    "make": "Toyota",
    "color": "White",
    "year": 2023
}

car_json = json.dumps(car)

print(car_json)


