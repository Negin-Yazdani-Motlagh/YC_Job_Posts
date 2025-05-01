import json
from pathlib import Path

def extract_2022_posts():
    # Create output directory
    output_dir = Path("2022_Analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Read the yearly filtered job posts
    with open("Filtered_Nested_Jobs/filtered_nested_job_posts_yearly.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract 2022 posts
    if "2022" in data["YC"]:
        # Create new structure with only 2022 data
        posts_2022 = {
            "YC": {
                "2022": data["YC"]["2022"]
            }
        }
        
        # Save to new file
        output_file = output_dir / "2022_job_posts.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts_2022, f, indent=4)
        
        print(f"Extracted {len(posts_2022['YC']['2022']['comments'])} posts from 2022")
        print(f"Saved to: {output_file}")
    else:
        print("No 2022 posts found in the data")

if __name__ == "__main__":
    extract_2022_posts() 
