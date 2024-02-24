# modifying methods

# split and sub

# sub - replaces a sequence in a string with a repl string
# or with the return string or a repl function

import re

string = "Abccc123+*Abc_+*Ab1-2345*+Ab+*Ab"

pattern = re.compile(r".2\d*")

string_subbed = pattern.sub("REGEX", string)

print(string_subbed)