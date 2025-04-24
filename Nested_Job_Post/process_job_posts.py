import json
from bs4 import BeautifulSoup
from pathlib import Path
import re
from datetime import datetime

def extract_month_year(title):
    # Extract month and year from title
    match = re.search(r'\((\w+)\s+(\d{4})\)', title)
    if match:
        month, year = match.groups()
        # Convert month name to number
        month_num = datetime.strptime(month, '%B').month
        return f"{year}-{month_num:02d}"
    return None

def process_html_content():
    # Create output directory if it doesn't exist
    output_dir = Path("Nested_Job_Post")
    output_dir.mkdir(exist_ok=True)
    
    # Read the HTML content JSON file
    with open("HTML_who_is_hiring/hiring_posts_html.json", 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    # Initialize nested data structure
    nested_data = {"YC": {}}
    
    # Process each post
    for post in posts:
        try:
            print(f"Processing: {post['title']}")
            
            # Extract month-year key
            month_year = extract_month_year(post['title'])
            if not month_year:
                print(f"Could not extract date from title: {post['title']}")
                continue
            
            # Parse HTML content
            soup = BeautifulSoup(post['html_content'], 'html.parser')
            
            # Find all comments
            articles = soup.find_all(class_="athing")
            
            # Extract top-level comments
            top_level_comments = []
            for article in articles:
                commtext = article.find(class_="commtext")
                ind = article.find(class_="ind")
                if commtext and ind and ind.get("indent") == "0":
                    # Get the text content and clean it
                    text = commtext.get_text(strip=True)
                    # Remove any "reply" or "flag" links that might be included
                    text = re.sub(r'\s*\[reply\]\s*|\s*\[flag\]\s*', '', text)
                    top_level_comments.append(text)
            
            # Add to nested structure
            nested_data["YC"][month_year] = {
                "comments": top_level_comments,
                "numJobPost": len(top_level_comments)
            }
            
        except Exception as e:
            print(f"Error processing {post['title']}: {str(e)}")
            continue
    
    # Save the nested data
    output_file = output_dir / "nested_job_posts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(nested_data, f, indent=4)
    
    print(f"\nSuccessfully processed {len(posts)} posts")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    process_html_content() 
