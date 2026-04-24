import subprocess
import sys

from pathlib import Path
from prefect import flow, task

def run_script(path): 
    base_path = Path(__file__).parent.parent
    script_path = base_path / path

    return subprocess.run(
        [sys.executable, str(script_path)],
        check = True, 
        cwd = str(base_path)
    )

@task 
def run_scrapy(): 
    base_path = Path(__file__).parent.parent
    scrapy_dir = base_path / "scraping" / "hn_scraper"

    subprocess.run(
        ["scrapy", "crawl", "topstories", "-O", "hn_raw.json"], 
        check = True, 
        cwd=str(scrapy_dir)
    )

@task 
def load_raw(): 
    run_script("etl/load_raw.py")

@task
def transform_clean(): 
    run_script("etl/transform_clean.py")

@task
def build_analysis(): 
    run_script("etl/build_analysis.py")

@flow(name = "Hacker News Pipeline")
def hn_pipeline(): 
    run_scrapy()
    load_raw()
    transform_clean()
    build_analysis()

if __name__ == "__main__": 
    try: 
        hn_pipeline()
    except Exception as e: 
        print(f"Pipeline Burst: {e}")