import csv

filename = 'students.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        # print(row) # ['Ruslan', '24B202424', '1', 'ruslan@kbtu.kz']
                     # ['Mariya', '24B202425', '1', 'mariya@kbtu.kz']
        name, id, study_year, email = row
        print(name, id, study_year, email) # Ruslan 24B202424 1 ruslan@kbtu.kz
                                           # Mariya 24B202425 1 mariya@kbtu.kz
