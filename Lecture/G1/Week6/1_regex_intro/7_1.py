# escaping characters

# [ ] - used to make a set of characters

import re

string = "Abccc123+* Abc_+*Ab12345*+Ab\n +*Ab"

matches = re.finditer(r"[Abc]", string) # looking for one A, b or c

for match in matches:
    print(match)

