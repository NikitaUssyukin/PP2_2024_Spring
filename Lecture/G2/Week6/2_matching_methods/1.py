# re methods
# methods to search for matches:
# match, findall, fullmatch, search, finditer

import re 

word = "roses are red, violets are blue"

print("match: ", re.match("r..", word))

print("findall: ", re.findall("r..", word))

word = "red"

print("fullmatch: ", re.fullmatch("r..", word))

word = "roses are red, violets are blue"

print("search: ", re.search("re", word))

print("finditer: ", re.finditer("re", word))
