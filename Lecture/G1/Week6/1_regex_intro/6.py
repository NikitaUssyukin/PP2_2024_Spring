# escaping characters

# \ - used to escape characters, such as meta characters

import re

string = "Abccc123+* Abc_+*Ab12345*+Ab\n +*Ab"

matches = re.finditer(r"\+\*", string) # looking for a literal + followed by a literal *

for match in matches:
    print(match)

