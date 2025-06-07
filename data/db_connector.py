import pandas as pd
import psycopg2
import os

def fetch_postgres_data(query):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df