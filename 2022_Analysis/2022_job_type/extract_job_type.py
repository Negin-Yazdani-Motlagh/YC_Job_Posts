import json
import re
import pandas as pd
from pathlib import Path

# List of job type keywords to search for (case-insensitive)
JOB_TYPE_KEYWORDS = [
    # Remote work variations
    "Remote", "Remote-friendly", "Remote-first", "Remote-only", "Work From Home", "WFH", "Telecommute",
    # Location variations
    "On-site", "Onsite", "On site", "Hybrid", "Flexible Location", "Distributed Team", "Global Remote",
    # Employment type variations
    "Full-time", "Full time", "Fulltime", "Part-time", "Part time", "Parttime", "Contract", "Freelance",
    "Temporary", "Internship", "Seasonal", "Volunteer", "Per Diem", "Hourly", "Consultant",
    # Schedule variations
    "Flexible Hours", "Fixed Schedule", "Shift Work", "Night Shift", "Weekend Shift",
    "Rotating Shift", "Compressed Workweek",
    # Employment status variations
    "W-2", "1099", "Corp-to-Corp", "C2C", "Payroll", "Intern (Paid)", "Intern (Unpaid)", "Apprenticeship",
    # Additional variations
    "Must relocate", "Visa sponsorship available", "No sponsorship"
]

def extract_job_types(header: str) -> str:
    found_types = []
    header_lower = header.lower()
    
    # First pass: look for exact matches
    for keyword in JOB_TYPE_KEYWORDS:
        if keyword.lower() in header_lower:
            found_types.append(keyword)
    
    # Second pass: look for variations with special characters
    if "onsite" in header_lower and "On-site" not in found_types and "Onsite" not in found_types:
        found_types.append("On-site")
    if "remote" in header_lower and "Remote" not in found_types:
        found_types.append("Remote")
    if "hybrid" in header_lower and "Hybrid" not in found_types:
        found_types.append("Hybrid")
    if "fulltime" in header_lower or "full time" in header_lower and "Full-time" not in found_types:
        found_types.append("Full-time")
    
    return " | ".join(found_types) if found_types else "Unknown"

def main():
    # Load posts
    with open("2022_Analysis/2022_job_posts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    posts = data["YC"]["2022"]["comments"]

    results = []
    print("\nSample job type detection results:")
    print("-" * 50)
    for idx, post in enumerate(posts):
        header = post.split('\n')[0]
        job_types = extract_job_types(header)
        results.append({
            "Post #": idx + 1,
            "Job Type": job_types
        })
        # Print first 5 posts for verification
        if idx < 5:
            print(f"\nPost #{idx + 1}:")
            print(f"Header: {header}")
            print(f"Detected Job Types: {job_types}")

    df = pd.DataFrame(results)
    output_file = Path("2022_Analysis/2022_job_type/2022_job_type_details.xlsx")
    df.to_excel(output_file, index=False)
    print(f"\nSaved job type details to: {output_file}")

if __name__ == "__main__":
    main() 
