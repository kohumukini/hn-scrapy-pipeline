import requests
from datetime import datetime, UTC

def fetch_top_stories(limit = 30): 
    ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:limit]

    stories = []
    for story_id in ids: 
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/topstories.json/{story_id}.json")
        data = response.json()

        stories.append({
            "story_id" : story_id, 
            "title" : data.get("title"), 
            "url" : data.get("url"), 
            "score" : data.get("score"), 
            "author": data.get("by"), 
            "time" : data.get("time"), 
            "scraped_at": datetime.now(UTC).isoformat()
        })

    return stories