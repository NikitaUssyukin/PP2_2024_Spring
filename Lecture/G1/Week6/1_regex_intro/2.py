# meta characters
# * + . ? | ( ) [ ] { } ^ $ \
# * - 0 or more occurences
# + - 1 or more occurences
# . - any character (except a new line)
# | - either or

import re

string = "AbcccabcAbgh"

print(re.findall("bc*", string))

print(re.findall("bc+", string))
print(re.findall("b..", string))

sentence = "roses are red, violets are blue"

print(re.findall("roses|violets", sentence))

