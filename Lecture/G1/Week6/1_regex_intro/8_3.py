# grouping

# ( ) - used to group patterns

import re

file = open("dates.txt", "r")

dates = file.read()

matches = re.finditer(r"(\d{2}[-/._ ]){2}(\d{4})", dates) 
# group:                      1             2             
for match in matches:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print("--------------")

