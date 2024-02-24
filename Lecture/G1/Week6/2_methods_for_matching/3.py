import re

# findall, match, fullmatch, search, finditer, compile

# compile - accepts a regex pattern and return a regex object
string = "Abccc123 Abc_Ab12345Ab\n Ab"

pattern = re.compile("Abc")

print(pattern)

print(pattern.findall(string))