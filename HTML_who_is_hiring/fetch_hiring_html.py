import json
import requests
from pathlib import Path
import time
from bs4 import BeautifulSoup

def fetch_html_content():
    # Create output directory if it doesn't exist
    output_dir = Path("HTML_who_is_hiring")
    output_dir.mkdir(exist_ok=True)
    
    # Read the all_hiring_posts.json file
    with open("who_is_Hiring/all_hiring_posts.json", 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    # Initialize list to store HTML content
    html_data = []
    
    # Fetch HTML content for each URL
    for post in posts:
        try:
            print(f"Fetching HTML for: {post['title']}")
            
            # Add headers to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Fetch the page content
            response = requests.get(post['url'], headers=headers, timeout=30)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Store the data
            html_data.append({
                'title': post['title'],
                'url': post['url'],
                'html_content': str(soup)
            })
            
            # Add a delay to be respectful to the server
            time.sleep(2)
            
        except Exception as e:
            print(f"Error fetching {post['url']}: {str(e)}")
            continue
    
    # Save the HTML content to a JSON file
    output_file = output_dir / "hiring_posts_html.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(html_data, f, indent=2)
    
    print(f"\nSuccessfully fetched HTML content for {len(html_data)} posts")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    fetch_html_content() 
