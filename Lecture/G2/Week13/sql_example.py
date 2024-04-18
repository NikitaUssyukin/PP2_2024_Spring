# SQL

# Create - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE

# Create a new table - CREATE TABLE


import psycopg2

# Connect to the database and get the connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='students', 
    user='postgres', 
    password='1234'
    )

# Create a cursor to work with our DB
cur = conn.cursor()

# Delete a table with students
cur.execute('DROP TABLE students_data;')

conn.commit()

# Create a table for students data
cur.execute("""CREATE TABLE students_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            study_year INT,
            gpa FLOAT
);
""")

conn.commit()

# Creating new rows in that table (inserting data)
cur.execute("""INSERT INTO students_data (name, id, study_year, gpa) VALUES
            ('Timur', '23B202323', 1, 3.0),
            ('Sayat', '23B212323', 1, 3.7);
""")

conn.commit()

# Reading all data from the database
cur.execute('SELECT * FROM students_data;')

print(cur.fetchall())
# or
# print(cur.fetchone())
# print(cur.fetchone())

# Updating data
cur.execute("""UPDATE students_data
            SET gpa = 4.0
            WHERE id = '23B202323'; 
""")

conn.commit()

# Deleting data
cur.execute("""DELETE FROM students_data
            WHERE id = '23B212323'; 
""")

conn.commit()