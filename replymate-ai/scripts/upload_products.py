import csv
import psycopg2
import os

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

with open("products.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute("INSERT INTO products (name, description) VALUES (%s, %s)", (row["name"], row["description"]))

conn.commit()
cur.close()
conn.close()
print("Products uploaded successfully.")
