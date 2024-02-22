# meta characters
# * + . \ ? [ ] { } ( ) ^ $ |
# ^ - (caret) match only at the beginning
# $ - match only at the end

import re 

word = "Abc AbAbccccabcAbb"

print(re.findall("^Ab+", word))

print(re.findall("Ab+$", word))