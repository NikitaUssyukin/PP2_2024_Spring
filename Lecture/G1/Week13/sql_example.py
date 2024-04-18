# CRUD - Create, Read, Update, Delete

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

import psycopg2

# connecting to students database
conn = psycopg2.connect(
    host="localhost", 
    dbname="students", 
    user="postgres", 
    password="1234"
    )

# creating a cursor
# cursor is needed to interact with the database
cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()') # Executing the query inside the single quotes 
                                # in our connected database
db_ver = cur.fetchall() # Getting all data that we got from the last query
print(db_ver)

# Create a table with students
cur.execute("""CREATE TABLE students_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            study_year INT,
            email VARCHAR(255)
            );
""")

conn.commit()

# Create - INSERT
cur.execute("""INSERT INTO students_data (name, id, study_year, email) VALUES 
            ('Timur', '23B202323', 1, 'timur@kbtu.kz'),
            ('Sayat', '23B212323', 1, 'sayat@kbtu.kz');
            """)

conn.commit()

# Read - SELECT
cur.execute('SELECT * FROM students_data')
query_data = cur.fetchall() # returns a list with individual rows as tuples
print(query_data) # [('Timur', '23B202323', 1, 'timur@kbtu.kz'), ('Sayat', '23B212323', 1, 'sayat@kbtu.kz')]

query_data = cur.fetchall() 
print(query_data) # []

cur.execute('SELECT * FROM students_data')
query_row = cur.fetchone() # returns one row as a tuple
print(query_row) # ('Timur', '23B202323', 1, 'timur@kbtu.kz')
query_row = cur.fetchone() 
print(query_row) # ('Sayat', '23B212323', 1, 'sayat@kbtu.kz')

# Update - UPDATE
cur.execute("""UPDATE students_data
            SET email = 'timur_sh@kbtu.kz'
            WHERE id = '23B202323';
""")

conn.commit()

# Delete - DELETE
cur.execute("DELETE FROM students_data WHERE id = '23B202323';")

conn.commit()
