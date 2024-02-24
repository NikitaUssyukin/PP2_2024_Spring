import re, csv

file = open("row.txt", "r", encoding="utf8")

text = file.read()

pattern = re.compile(r"\n(?P<order>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n")

results = pattern.finditer(text)

with open("data.csv", "w", newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["order", "name", "count", "price"])
    for result in results:
        writer.writerow([
            result.group('order'),
            result.group('name'),
            result.group('count').strip().replace(',', '.'),
            result.group('price').strip().replace(',', '.').replace(' ', ''),
        ])