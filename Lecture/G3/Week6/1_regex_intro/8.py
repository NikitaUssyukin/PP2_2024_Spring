# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# ( ) - grouping

import re

word = r"R0ses are r3d, v1olets are blu3"

pattern = re.compile(r"([a-zA-Z0-9]{2})+")

matches = pattern.finditer(word)

for match in matches:
    print(match.group())


