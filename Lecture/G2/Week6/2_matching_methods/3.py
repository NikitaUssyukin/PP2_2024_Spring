# re methods
# methods to search for matches:
# match, findall, fullmatch, search, finditer

import re 

word = "roses are red, violets are blue"

matches = re.finditer("re", word)

for match in matches:
    print(match)

