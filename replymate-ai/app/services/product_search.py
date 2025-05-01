import psycopg2
import os
import numpy as np
from openai import OpenAI

def search_products(query_embedding, top_k=3):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, description
        FROM products
        ORDER BY embedding <-> %s
        LIMIT %s;
    """, (query_embedding, top_k))

    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
