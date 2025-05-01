import json
from pathlib import Path

def extract_2015_posts():
    # Create output directory
    output_dir = Path("2015_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2015 posts
    if "2015" in data["YC"]:
        # Create new structure with only 2015 data
        posts_2015 = {
            "YC": {
                "2015": data["YC"]["2015"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2015_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2015, f, indent=4)
        
        print(f"Extracted {len(posts_2015['YC']['2015']['comments'])} posts from 2015")
        print(f"Saved to: {output_file}")
    else:
        print("No 2015 posts found in the data")

if __name__ == "__main__":
    extract_2015_posts() 
