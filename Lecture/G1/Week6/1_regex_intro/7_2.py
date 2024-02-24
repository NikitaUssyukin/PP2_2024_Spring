# escaping characters

# [ ] - used to make a set of characters

import re

string = "Abccc123+* Abc_+*Ab12345*+Ab\n +*Ab"

matches = re.finditer(r"[a-z]", string) # looking for one letter from a to z

for match in matches:
    print(match)

