import json
from pathlib import Path
import re

def count_words(text):
    # Split text into words and count them
    return len(text.split())

def remove_html_tags(text):
    # Remove HTML tags using regex
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def filter_short_posts():
    # Create output directory
    output_dir = Path("Filtered_Nested_Jobs")
    output_dir.mkdir(exist_ok=True)
    
    # Read the nested job posts
    with open("Nested_Job_Post/nested_job_posts.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize new structure for filtered posts
    filtered_posts = {"YC": {}}
    
    # Process each month
    for month_year, month_data in data["YC"].items():
        filtered_comments = []
        
        # Filter out comments with 20 words or less and remove HTML tags
        for comment in month_data["comments"]:
            # Remove HTML tags
            clean_comment = remove_html_tags(comment)
            # Only include if more than 20 words (filter out short posts)
            if count_words(clean_comment) > 20:
                filtered_comments.append(clean_comment)
        
        # Only add month if it has filtered posts
        if filtered_comments:
            filtered_posts["YC"][month_year] = {
                "comments": filtered_comments,
                "numJobPost": len(filtered_comments)
            }
    
    # Save the filtered data
    output_file = output_dir / "filtered_nested_job_posts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_posts, f, indent=4)
    
    print(f"Found {sum(len(month['comments']) for month in filtered_posts['YC'].values())} posts after filtering out short posts (20 words or less)")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    filter_short_posts() 
