# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# . - any symbol
# ^ - matches only at the beginning of the string
# $ - matches only at the end of the string

import re

word = "AAbbAbbbbabbbb"

print(re.findall("ab*$", word))

print(re.findall("A.+", word))

print(re.findall("^Ab?", word))