# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# {n} - n number of occurences
# {n,m} - from n to m number of occurences

import re

word = "R0ses are r3d, v1olets are blu3"

print(re.findall("[a-zA-Z0-9]{2}", word))
print(re.findall("[a-zA-Z0-9]{2,6}", word))