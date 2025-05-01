import json
from pathlib import Path

def extract_2023_posts():
    # Create output directory
    output_dir = Path("2023_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2023 posts
    if "2023" in data["YC"]:
        # Create new structure with only 2023 data
        posts_2023 = {
            "YC": {
                "2023": data["YC"]["2023"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2023_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2023, f, indent=4)
        
        print(f"Extracted {len(posts_2023['YC']['2023']['comments'])} posts from 2023")
        print(f"Saved to: {output_file}")
    else:
        print("No 2023 posts found in the data")

if __name__ == "__main__":
    extract_2023_posts() 
