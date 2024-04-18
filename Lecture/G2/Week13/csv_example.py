import psycopg2
import csv

filename = 'students.csv'

csvfile = open(filename, "r")

csvreader = csv.reader(csvfile, delimiter=',')

for row in csvreader:
    print(row)
    name, id, study_year, gpa = row
    print(name, id, study_year, gpa)

