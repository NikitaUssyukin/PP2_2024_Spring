# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# ( ) - grouping

import re

word = r"R0ses are r3d, v1olets are blu3"

print(re.findall(r"([a-zA-Z0-9]{2})", word))
print(re.findall(r"([a-zA-Z0-9]{2})+", word))