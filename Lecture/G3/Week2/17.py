ourdict = {
    "Car1": {
        "Make": "Ford",
        "Model": "Mustang",
        "Year": 1966,
        "Color": "Red",
    },
    "Car2": {
        "Make": "Toyota",
        "Model": "Camry",
        "Year": 2018,
        "Color": "White",
    },
    "Car3": {
        "Make": "Porsche",
        "Model": "911 Carrera Turbo S (992)",
        "Year": 2023,
        "Color": "Green",
    },
}

print(ourdict)

print("---")

ourdict.pop("Car2")
ourdict.update({
    "Car2": {
        "Make": "Porsche",
        "Model": "911 Carrera Turbo S (992)",
        "Year": 2023,
        "Color": "Green",
    },
})
ourdict.pop("Car3")
print(ourdict)




