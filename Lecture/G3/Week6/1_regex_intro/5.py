# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# [ ] - set of symbols

import re

word = "R0ses are r3d, v1olets are blu3"

print(re.findall("[abc]", word))

print(re.findall("[a-z]", word))

print(re.findall("[a-zA-Z0-9]", word))
