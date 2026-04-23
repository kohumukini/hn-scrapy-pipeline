CREATE TABLE hn_clean (
    story_id TEXT PRIMARY KEY, 
    title TEXT, 
    url TEXT, 
    score INT, 
    author TEXT, 
    age TEXT, 
    scraped_at TIMESTAMP
); 