import json

car_json = '{"make": "Lexus", "model": "LFA", "color": "gray"}'

car = json.loads(car_json)

print(car)