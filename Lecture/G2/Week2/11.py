ourdict = {
    "Dog": 100,
    "Cat": 50,
    "Elephant": 2,
}

print(ourdict)

ourdict["Dog"] = 10

ourdict["Cat"] -= 20

for x in ourdict:
    print(x, ourdict[x])