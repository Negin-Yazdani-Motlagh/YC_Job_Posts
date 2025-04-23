import json
from pathlib import Path

def count_words(text):
    # Split text into words and count them
    return len(text.split())

def filter_short_posts():
    # Create output directory
    output_dir = Path("30_words_posts")
    output_dir.mkdir(exist_ok=True)
    
    # Read the nested job posts
    with open("Nested_Job_Post/nested_job_posts.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize new structure for short posts
    short_posts = {"YC": {}}
    
    # Process each month
    for month_year, month_data in data["YC"].items():
        short_comments = []
        
        # Filter comments with 30 words or less
        for comment in month_data["comments"]:
            if count_words(comment) <= 30:
                short_comments.append(comment)
        
        # Only add month if it has short posts
        if short_comments:
            short_posts["YC"][month_year] = {
                "comments": short_comments,
                "numJobPost": len(short_comments)
            }
    
    # Save the filtered data
    output_file = output_dir / "0_30_words_posts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(short_posts, f, indent=4)
    
    print(f"Found {sum(len(month['comments']) for month in short_posts['YC'].values())} posts with 30 words or less")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    filter_short_posts() 
