CREATE TABLE raw_hn ( 
    id SERIAL PRIMARY KEY, 
    scraped_at TIMESTAMP, 
    payload JSONB
); 