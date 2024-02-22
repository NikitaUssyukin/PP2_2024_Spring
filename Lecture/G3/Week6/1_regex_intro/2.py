# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# quantifiers
# * - 0 or more occurences
# + - 1 or more occurences
# ? - 0 or 1 occurence

import re

word = "AAbbAbbbbabbbb"

print(re.findall("Ab*", word))

print(re.findall("Ab+", word))

print(re.findall("Ab?", word))