import re

# findall, match, fullmatch, search, finditer, compile

# findall - find all matches in the string, returns a list of strs
# match - finds the match only at the beginning in the string, returns a match object
# search - finds the match anywhere in the string, returns a match object
# fullmatch - checks it the whole string matches the pattern, returns a match object

string = "Abccc123 Abc_Ab12345Ab\n Ab"

print(re.match("Abc", string)) # <re.Match object; span=(0, 3), match='Abc'>
print(re.match("123", string)) # None

print(re.search("Abc", string)) # <re.Match object; span=(0, 3), match='Abc'>
print(re.search("123", string)) # <re.Match object; span=(5, 8), match='123'>

print(re.fullmatch("Abc", string)) # None
print(re.fullmatch("Abccc123 Abc_Ab12345Ab\n Ab", string)) # <re.Match object; span=(0, 26), match='Abccc123 Abc_Ab12345Ab\n Ab'>