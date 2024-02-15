import json

car = {
    "make": "Subaru",
    "model": "Impreza",
    "year": 1995
}

car_json = json.dumps(car)

print(car_json)