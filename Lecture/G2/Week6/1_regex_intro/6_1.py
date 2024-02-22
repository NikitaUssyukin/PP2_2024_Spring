# meta characters
# * + . \ ? [ ] { } ( ) ^ $ |
# . - any character

import re 

word = "AbcAbAbccccabc"

print(re.findall("...", word))