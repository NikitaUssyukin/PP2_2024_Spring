import re

string = "Abccc123 Abc_Ab12345Ab\n Ab"

match_object = re.match("Abc", string)

print(match_object, match_object.group(), sep="\n")
print(match_object.span(), match_object.start(), match_object.end(), sep="\n")
print(match_object.string)

