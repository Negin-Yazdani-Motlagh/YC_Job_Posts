import json
import os
from pathlib import Path

def combine_hiring_posts():
    # Initialize an empty list to store all posts
    all_posts = []
    
    # Get the directory path
    base_dir = Path("who_is_Hiring")
    
    # Iterate through each year directory (2012-2024)
    for year in range(2012, 2025):
        year_dir = base_dir / str(year)
        json_file = year_dir / f"hiring_posts_{year}.json"
        
        if json_file.exists():
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    posts = json.load(f)
                    # Only keep title and URL for each post
                    simplified_posts = [{"title": post["title"], "url": post["url"]} for post in posts]
                    all_posts.extend(simplified_posts)
            except Exception as e:
                print(f"Error reading {json_file}: {e}")
    
    # Save combined posts to a new file
    output_file = base_dir / "all_hiring_posts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_posts, f, indent=2)
    
    print(f"Successfully combined {len(all_posts)} posts into {output_file}")

if __name__ == "__main__":
    combine_hiring_posts() 
