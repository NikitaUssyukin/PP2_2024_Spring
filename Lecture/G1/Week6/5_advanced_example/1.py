file = open("row.txt", "r", encoding="utf8")

for row in file:
    if "БИН" in row:
        print(row.split()[1].strip())