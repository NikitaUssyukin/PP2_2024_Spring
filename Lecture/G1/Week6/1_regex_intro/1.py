import re

string = "AbcccabcAb"

print(re.findall("Ab", string))

print(re.findall("bc*", string))