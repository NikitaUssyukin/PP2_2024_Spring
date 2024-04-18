# Relational Databases

# Data is stored in tables (also called relations)
# Tables consist of rows and columns

# In general, each table represents 1 entity type (e.g. student)
# Columns represent attributes of that entity
# Rows are instances of that entity (also called tuples or records)

# In such database, we can:
# Create data
# Read data
# Update data
# Delete data
# Or usually refered to as CRUD

# RDBMS - Relational Database Management System
# We will PostgeSQL (also known as Postgres) as our RDBMS 

# SQL - Structured Query Language
# It is the language used to work with RDBMS

# To start, we need:
# - Download and install PostreSQL
#   - During installation you can leave everything on default
#   - Remember/Write down the password that you set during the installation
# - Install psycopg2 package
#   - pip install psycopg2 (or pip3)
#   - or
#   - pip install psycopg2-binary (or pip3)

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

# Getting data from the DB
cur.execute('SELECT version()') # Will give us the version of our Postgres
db_ver = cur.fetchall() # Getting all data received by the query
print(db_ver)