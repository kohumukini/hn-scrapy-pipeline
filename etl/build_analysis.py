import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()
DB_CONN = os.getenv("DB_CONN")

def refresh_analysis(): 
    with psycopg2.connect(DB_CONN) as conn: 
        with conn.cursor() as cursor: 

            cursor.execute("REFRESH MATERIALIZED VIEW hn_analysis")

if __name__ == "__main__": 
    try: 
        refresh_analysis()
    except Exception as e: 
        print(f"Analysis Failed: {e}")