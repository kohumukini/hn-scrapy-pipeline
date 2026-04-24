import json
import psycopg2
import os

from dotenv import load_dotenv
from psycopg2.extras import Json
from datetime import datetime, UTC

DB_CONN = os.getenv("DB_CONN")

def load_raw(json_path): 
    with psycopg2.connect(DB_CONN) as conn: 
        with conn.cursor() as cursor: 
            with open(json_path) as file_in: 
                data = json.load(file_in)

            rows_to_insert = [
                (datetime.fromisoformat(item["scraped_at"]), Json(item))
                for item in data
            ] 

            from psycopg2.extras import execute_batch
            execute_batch(cursor, """
                INSERT INTO raw_hn (scraped_at, payload)
                VALUES (%s, %s)              
            """, rows_to_insert)   

if __name__ == "__main__": 
    load_raw("hn_raw.json")