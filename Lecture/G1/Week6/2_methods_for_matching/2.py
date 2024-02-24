import re

# findall, match, fullmatch, search, finditer

# finditer - find all matches in the string, returns an iterator, 
# which you can use to iterate over match objects

string = "Abccc123 Abc_Ab12345Ab\n Ab"

matches = re.finditer("Abc*", string)

for match in matches:
    print(match)
    print(match.group())
    print(match.span())
    print("----------")
