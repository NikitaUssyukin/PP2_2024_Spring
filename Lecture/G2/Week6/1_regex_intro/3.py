# meta characters
# * + . \ ? [ ] { } ( ) ^ $ |
# * - 0 or more occurences

import re 

word = "AbcAbAbccccabc"

print(re.findall("Abc*", word))