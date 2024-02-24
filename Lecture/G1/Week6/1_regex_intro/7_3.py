# escaping characters

# [ ] - used to make a set of characters

import re

string = "Abccc123+* Abc_+*Ab1-2345*+Ab\n +*Ab"

matches = re.finditer(r"[a-zA-Z0-9- ]", string) # looking for: one letter from a to z or from A to Z,
# or one digit from 0 to 9, or for a literal dash or a space

for match in matches:
    print(match)

