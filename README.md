# Hacker News ETL Pipeline

A Python-based data pipeline that scrapes top stories from Hacker News, stores them in a PostgreSQL "Bronze" layer (Raw JSON), and transforms them into a "Silver" layer (Cleaned SQL) for visualization in Tableau.

## 📁 Project Structure
- `scraping/`: Contains the Scrapy spider and API scrapers.
- `etl/`: Python scripts for loading (`load_raw.py`) and transforming (`transform_raw.py`) data.
- `db/`: SQL schema definitions for Raw, Clean, and Analysis layers.
- `config/`: Environment and configuration files.
- `.env`: (Ignored by git) Stores database credentials and connection strings.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Database:** PostgreSQL
- **Libraries:** Scrapy, Psycopg2, Python-dotenv, Requests
- **Visualization:** Tableau

## 🚀 How It Works

### 1. Extraction (Scraping)
Run the spider to generate the raw data file:
```bash
cd scraping/hn_scraper
scrapy crawl topstories -o hn_raw.json