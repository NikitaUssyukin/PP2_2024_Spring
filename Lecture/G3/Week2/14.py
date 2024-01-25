ourdict = {
    "Make": "Ford",
    "Model": "Mustang",
    "Year": 1966,
    "Color": "Red",
}

print(ourdict)
print(ourdict["Make"])

ourdict["Color"] = "Yellow"
print(ourdict["Color"])

for key in ourdict:
    print(ourdict[key])

for value in ourdict.values():
    print(value)

for key, value in ourdict.items():
    print(key,":", value)