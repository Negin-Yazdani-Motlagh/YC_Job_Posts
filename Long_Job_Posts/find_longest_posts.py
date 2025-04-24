import json
from pathlib import Path
from bs4 import BeautifulSoup
import re

def clean_html_content(html_content):
    # Remove HTML tags and clean the content
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def find_longest_posts():
    # Read the nested job posts
    with open("Nested_Job_Post/nested_job_posts.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize results
    longest_posts = {}
    
    # Process each month
    for month_year, month_data in data["YC"].items():
        # Clean posts and find the longest one for this month
        longest_post = ""
        max_length = 0
        
        for post in month_data["comments"]:
            cleaned_post = clean_html_content(post)
            if len(cleaned_post) > max_length:
                max_length = len(cleaned_post)
                longest_post = cleaned_post
        
        if longest_post:  # Only include months with posts
            longest_posts[month_year] = {
                "length": max_length,
                "content": longest_post
            }
    
    # Create output directory
    output_dir = Path("Long_Job_Posts")
    output_dir.mkdir(exist_ok=True)
    
    # Save results
    with open(output_dir / "longest_posts.json", 'w', encoding='utf-8') as f:
        json.dump(longest_posts, f, indent=4)
    
    # Print summary
    print("\nLongest Job Posts by Date:")
    print("-" * 30)
    for date, info in longest_posts.items():
        print(f"{date}: {info['length']} characters")
    
    print(f"\nResults saved to: {output_dir / 'longest_posts.json'}")

if __name__ == "__main__":
    find_longest_posts() 
