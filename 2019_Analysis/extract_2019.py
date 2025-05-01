import json
from pathlib import Path

def extract_2019_posts():
    # Create output directory
    output_dir = Path("2019_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2019 posts
    if "2019" in data["YC"]:
        # Create new structure with only 2019 data
        posts_2019 = {
            "YC": {
                "2019": data["YC"]["2019"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2019_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2019, f, indent=4)
        
        print(f"Extracted {len(posts_2019['YC']['2019']['comments'])} posts from 2019")
        print(f"Saved to: {output_file}")
    else:
        print("No 2019 posts found in the data")

if __name__ == "__main__":
    extract_2019_posts() 
