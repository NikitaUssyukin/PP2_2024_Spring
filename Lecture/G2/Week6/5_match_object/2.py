# match object

import re 

word = "roses are red, violets are blue"

matches = re.finditer("roses|violets", word)

for match in matches:
    print(match.start())
    print(match.end())
    print(match.span())
