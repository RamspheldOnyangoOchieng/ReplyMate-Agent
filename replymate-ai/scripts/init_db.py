from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # Loads environment variables from .env file

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

with open("db/schema.sql", "r") as f:
    cur.execute(f.read())

with open("db/seed_data.sql", "r") as f:
    cur.execute(f.read())

conn.commit()
cur.close()
conn.close()

print("Database initialized successfully.")
