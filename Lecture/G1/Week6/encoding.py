# Doesn't work without utf8

file1 = open("row.txt", "r")

text = file1.read()

# And here it works

file2 = open("row.txt", "r", encoding="utf8")

text_utf8 = file2.read()

print(text_utf8, end="\n------------------------\n")