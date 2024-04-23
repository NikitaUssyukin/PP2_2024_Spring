import csv
import psycopg2

# connecting to a database
conn = psycopg2.connect(
    host="localhost", 
    dbname="students", 
    user="postgres", 
    password="1234"
    )

# creating a cursor
# cursor is needed to interact with the database
cur = conn.cursor()

# csv file name
filename = 'students.csv'

# reading csv
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, id, study_year, email = row
        # insertind data into the table
        cur.execute(f"""
                    UPDATE students_data 
                    SET email='{email}'
                    WHERE id='{id}';
                    """)
    
    conn.commit()
        

