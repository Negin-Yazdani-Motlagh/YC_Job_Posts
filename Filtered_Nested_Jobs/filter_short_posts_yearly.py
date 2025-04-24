import json
from pathlib import Path
import re
from collections import defaultdict

def count_words(text):
    # Split text into words and count them
    return len(text.split())

def remove_html_tags(text):
    # Remove HTML tags using regex
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def extract_year(month_year):
    # Extract year from "YYYY-Month" format
    return month_year.split('-')[0]

def filter_short_posts_yearly():
    # Create output directory
    output_dir = Path("Filtered_Nested_Jobs")
    output_dir.mkdir(exist_ok=True)
    
    # Read the nested job posts
    with open("Nested_Job_Post/nested_job_posts.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize new structure for filtered posts
    filtered_posts = {"YC": {}}
    
    # Dictionary to store posts by year
    yearly_posts = defaultdict(list)
    
    # Process each month
    for month_year, month_data in data["YC"].items():
        year = extract_year(month_year)
        
        # Filter out comments with 20 words or less and remove HTML tags
        for comment in month_data["comments"]:
            # Remove HTML tags
            clean_comment = remove_html_tags(comment)
            # Only include if more than 20 words (filter out short posts)
            if count_words(clean_comment) > 20:
                yearly_posts[year].append(clean_comment)
    
    # Organize posts by year
    for year, comments in yearly_posts.items():
        if comments:  # Only add year if it has filtered posts
            filtered_posts["YC"][year] = {
                "comments": comments,
                "numJobPost": len(comments)
            }
    
    # Save the filtered data
    output_file = output_dir / "filtered_nested_job_posts_yearly.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_posts, f, indent=4)
    
    print(f"Found {sum(len(year['comments']) for year in filtered_posts['YC'].values())} posts after filtering out short posts (20 words or less)")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    filter_short_posts_yearly() 
