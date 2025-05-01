import json
from pathlib import Path

def extract_2020_posts():
    # Create output directory
    output_dir = Path("2020_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2020 posts
    if "2020" in data["YC"]:
        # Create new structure with only 2020 data
        posts_2020 = {
            "YC": {
                "2020": data["YC"]["2020"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2020_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2020, f, indent=4)
        
        print(f"Extracted {len(posts_2020['YC']['2020']['comments'])} posts from 2020")
        print(f"Saved to: {output_file}")
    else:
        print("No 2020 posts found in the data")

if __name__ == "__main__":
    extract_2020_posts() 
