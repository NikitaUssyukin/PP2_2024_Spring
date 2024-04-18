# CRUD - Create, Read, Update, Delete

# Relational database
# Has tables (also called relations)
# Each table has rows and columns
# Rows are also called records or tuples
# Columns are also called attributes

# Each table, generally, represents 1 entity type (e.g. a student)
# Rows represent instances of this entity (individual students in our case)
# Columns represent values, attributed to those instances

# RDBMS - Relational DataBase Management System
# SQL - Structured Query Language

# As our RDBMS we're going to use PostgreSQL

# When installing Postgres, make sure to install all 4 sugested components (Server, pgAdmin, Stack Builder, Command Line Tools)
# And remember/write down the password that you specify

# Next, we need psycopg2 package:
# pip install psycopg2 
# or 
# pip3 install psycopg2
# or
# pip install psycopg2-binary
# or
# pip3 install psycopg2-binary

import psycopg2

# connecting to a database

conn = psycopg2.connect(
    host="localhost", 
    dbname="suppliers", 
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