import psycopg2

conn = psycopg2.connect(host="localhost", dbname="suppliers", user="postgres", password="1234")

cur = conn.cursor()