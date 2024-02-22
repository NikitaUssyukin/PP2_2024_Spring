# meta characters
# * + . \ ? [ ] { } ( ) ^ $ |
# + - 1 or more occurences

import re 

word = "AbcAbAbccccabc"

print(re.findall("Abc+", word))