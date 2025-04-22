import requests
import json
import os
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('URLs/html_save.log'),
        logging.StreamHandler()
    ]
)

# List of URLs to extract HTML from
urls = [
    "https://news.ycombinator.com/submitted?id=whoishiring",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=39562986&n=31",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=35773707&n=61",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=31947297&n=91",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=28380661&n=121",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=24969524&n=151",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=22225313&n=181",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=19543939&n=211",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=17205866&n=241",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=14901314&n=271",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=12627853&n=301",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=10655741&n=331",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=8822808&n=361",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=7162197&n=391",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=4857717&n=421",
    "https://news.ycombinator.com/submitted?id=whoishiring&next=2949790&n=451"
]

def get_page(url, session, retries=3):
    for attempt in range(retries):
        try:
            logging.info(f"Fetching {url} (attempt {attempt + 1}/{retries})")
            response = session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            if attempt < retries - 1:
                delay = (attempt + 1) * 10  # Exponential backoff
                logging.warning(f"Error fetching {url}: {str(e)}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error(f"Failed to fetch {url} after {retries} attempts: {str(e)}")
                return None

def main():
    # Create URLs directory if it doesn't exist
    os.makedirs('URLs', exist_ok=True)
    
    # Set up session with headers
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    })
    
    results = []
    
    for url in urls:
        html_content = get_page(url, session)
        if html_content:
            results.append({
                "url": url,
                "html": html_content,
                "timestamp": datetime.now().isoformat()
            })
            logging.info(f"Successfully saved HTML for {url}")
        else:
            results.append({
                "url": url,
                "html": None,
                "error": "Failed to fetch after multiple attempts",
                "timestamp": datetime.now().isoformat()
            })
        
        # Add delay between requests
        time.sleep(5)
    
    # Save results to JSON file
    output_path = os.path.join('URLs', 'html_content.json')
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
    
    logging.info(f"HTML content saved to {output_path}")

if __name__ == "__main__":
    main() 
