import json
from pathlib import Path

def extract_2017_posts():
    # Create output directory
    output_dir = Path("2017_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2017 posts
    if "2017" in data["YC"]:
        # Create new structure with only 2017 data
        posts_2017 = {
            "YC": {
                "2017": data["YC"]["2017"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2017_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2017, f, indent=4)
        
        print(f"Extracted {len(posts_2017['YC']['2017']['comments'])} posts from 2017")
        print(f"Saved to: {output_file}")
    else:
        print("No 2017 posts found in the data")

if __name__ == "__main__":
    extract_2017_posts() 
