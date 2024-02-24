# modifying methods

# split and sub

# sub - replaces a sequence in a string with a repl string
# or with the return string or a repl function

import re

string = "The rain in Spain"

pattern = re.compile(r"\b[a-zA-Z]+\b")

def repl(m):
    word = str(m.group())
    res = ""
    for i in range(len(word)):
        if i % 2 == 0:
            res += word[i].upper()
        else:
            res += word[i].lower()
    return res

string_subbed = pattern.sub(repl, string)

print(string_subbed)