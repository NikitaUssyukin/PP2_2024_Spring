# meta characters
# * + . \ ? [ ] { } ( ) ^ $ |
# ? - 0 or 1 occurence

import re 

word = "AbcAbAbccccabc"

print(re.findall("Abc?", word))