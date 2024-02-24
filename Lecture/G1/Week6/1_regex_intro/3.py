# meta characters
# * + . ? | ( ) [ ] { } ^ $ \

# Quantifiers

# * - 0 or more occurences (or {0,})
# + - 1 or more occurences (or {1,})
# ? - 0 or 1 occurence (or {0,1})
# {2} - exactly 2 occurences
# {1,3} - from 1 occurence to 3 occurences
# {1,} - at least 1 occurence (same as +)
# {,3} - no more than 3 occurences

import re

string = "AbcccabcAb"

print(re.findall("bc*", string))

print(re.findall("bc+", string))

print(re.findall("bc?", string))

print(re.findall("bc{2}", string))

print(re.findall("bc{1,3}", string))

print(re.findall("bc{1,}", string))