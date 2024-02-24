# special sequences

# \d - any decimal digit
# \D - any character besides decimal digits 

# \w - any alphanumeric character
# \W - any non-alpanumeric character

# \s - any whitespace character (a space, a newline, etc)
# \S - any non-whitespace character

# \b - match at the beginning or at the end of the word (e.g. \bain or ain\b or \bain\b)
# \B - match not at the beginning or at the end of the word (e.g. \Bain or ain\B or \Bain\B)

import re

string = "Abccc123 Abc_Ab12345Ab\n"

print(re.findall(r"\d", string))
print(re.findall(r"\D", string))

print(re.findall(r"\w", string))
print(re.findall(r"\W", string))

print(re.findall(r"\s", string))
print(re.findall(r"\S", string))

print(re.findall(r"\bAb", string))
print(re.findall(r"Ab\b", string))

# example of a raw string vs usual
print(r"\nHello!\tHow are you?", "\nHello!\tHow are you?")
