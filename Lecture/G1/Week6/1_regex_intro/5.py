# special sequences

# \b - match at the beginning or at the end of the word (e.g. \bain or ain\b or \bain\b)
# \B - match not at the beginning or at the end of the word (e.g. \Bain or ain\B or \Bain\B)

import re

string = "Abccc123 Abc_Ab12345Ab\n Ab"

print(re.findall(r"\bAb", string))
print(re.findall(r"Ab\b", string))
print(re.findall(r"\bAb\b", string))
print(re.findall(r"\BAb", string))
print(re.findall(r"Ab\B", string))
print(re.findall(r"\BAb\B", string))

