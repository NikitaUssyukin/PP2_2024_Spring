import csv

filename = 'students.csv'

csvfile = open(filename, "r")

csvreader = csv.reader(csvfile, delimiter=',')

for row in csvreader:
    # print(row) # ['Timur', '23B202323', '1', '3']
                 # ['Sayat', '23B212323', '1', '3.7']
    name, id, study_year, gpa = row
    print(name, id, study_year, gpa) # Timur 23B202323 1 3
                                     # Sayat 23B212323 1 3.7

