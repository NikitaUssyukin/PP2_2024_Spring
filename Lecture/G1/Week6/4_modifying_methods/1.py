# modifying methods

# split and sub

# split - returns a splitted string based on the regex

import re

string = "Abccc123+*Abc_+*Ab1-2345*+Ab+*Ab"

pattern = re.compile("23")

string_splitted = pattern.split(string)

print(string_splitted)