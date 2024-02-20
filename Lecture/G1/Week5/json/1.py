import json

car = {"make": "Lexus", "model":"LFA", "color":"gray"}

car_json = json.dumps(car)

print(car_json)