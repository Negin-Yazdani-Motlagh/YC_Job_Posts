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
    "Must relocate", "Visa sponsorship available", "No sponsorship", "Full relocation", "Sponsorship",
    "Relocation required", "Relocation assistance", "Temporary remote", "H-1B", "H1B", "H1-B",
    "H-1Bs", "H1Bs", "H1-Bs"
]

def normalize_job_type(job_type):
    """Normalize job types to avoid duplicates and standardize format"""
    job_type = job_type.lower()
    
    # Map of variations to standard terms
    standard_terms = {
        'wfh': 'Remote',
        'work from home': 'Remote',
        'telecommute': 'Remote',
        'telework': 'Remote',
        'remote work': 'Remote',
        'remote-based': 'Remote',
        'remote based': 'Remote',
        'work remotely': 'Remote',
        'remote position': 'Remote',
        'remote role': 'Remote',
        'remote job': 'Remote',
        
        'onsite': 'On-site',
        'on site': 'On-site',
        
        'full time': 'Full-time',
        'fulltime': 'Full-time',
        'full-time': 'Full-time',
        
        'part time': 'Part-time',
        'parttime': 'Part-time',
        'part-time': 'Part-time',
        
        'full relocation': 'Must relocate',
        'relocation required': 'Must relocate',
        'then move to': 'Must relocate',
        
        'sponsorship': 'Visa sponsorship available',
        'visa sponsorship': 'Visa sponsorship available',
        'h-1b': 'Visa sponsorship available',
        'h1b': 'Visa sponsorship available',
        'h1-b': 'Visa sponsorship available',
        'h-1bs': 'Visa sponsorship available',
        'h1bs': 'Visa sponsorship available',
        'h1-bs': 'Visa sponsorship available',
        'sponsor h-1b': 'Visa sponsorship available',
        'sponsor h1b': 'Visa sponsorship available',
        'sponsor h1-b': 'Visa sponsorship available',
        'sponsor h-1bs': 'Visa sponsorship available',
        'sponsor h1bs': 'Visa sponsorship available',
        'sponsor h1-bs': 'Visa sponsorship available',
    }
    
    return standard_terms.get(job_type, job_type.title())

def extract_job_types(header: str) -> str:
    found_types = set()  # Use set to avoid duplicates
    header_lower = header.lower()
    
    # First pass: look for exact matches
    for keyword in JOB_TYPE_KEYWORDS:
        if keyword.lower() in header_lower:
            found_types.add(normalize_job_type(keyword))
    
    # Context-aware detection
    if "not just remote" in header_lower:
        found_types.add("Hybrid")
        found_types.add("Must relocate")
        if "Remote" in found_types:  # Add temporary remote indication
            found_types.add("Temporary remote")
    
    # Handle temporary remote with required relocation
    if "start remote" in header_lower and "then move" in header_lower:
        found_types.add("Must relocate")
        found_types.add("Remote")
        found_types.add("Temporary remote")
    
    # Additional variations
    if any(x in header_lower for x in ["telework", "work from home", "wfh", "work remotely", 
                                      "work remote", "remote work", "remote position", 
                                      "remote role", "remote job", "remote team"]):
        found_types.add("Remote")
    
    # Relocation and sponsorship variations
    if any(x in header_lower for x in ["full relocation", "relocation required", 
                                      "must relocate", "then move to", "relocate to"]):
        found_types.add("Must relocate")
    
    # Visa sponsorship variations
    if any(x in header_lower for x in ["sponsorship", "visa sponsorship", "visa available", 
                                      "sponsor visa", "visa provided", "h-1b", "h1b", "h1-b",
                                      "h-1bs", "h1bs", "h1-bs", "sponsor h-1b", "sponsor h1b", 
                                      "sponsor h1-b", "sponsor h-1bs", "sponsor h1bs", "sponsor h1-bs"]):
        found_types.add("Visa sponsorship available")
    
    # Convert set to sorted list for consistent ordering
    found_types = sorted(list(found_types))
    return " | ".join(found_types) if found_types else "Unknown"

def main():
    # Load posts
    with open("2018_Analysis/2018_job_posts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    posts = data["YC"]["2018"]["comments"]

    results = []
    print("\nSample job type detection results:")
    print("-" * 50)
    for idx, post in enumerate(posts):
        header = post
        job_types = extract_job_types(header)
        results.append({
            "Post #": idx + 1,
            "Job Type": job_types
        })
        # Print first 5 posts for verification
        if idx < 5:
            print(f"\nPost #{idx + 1}:")
            print(f"Header: {header[:200]}...")  # Print first 200 chars
            print(f"Detected Job Types: {job_types}")
        
        # Print job #14 for debugging
        if idx == 13:  # 0-based index, so 13 is the 14th job
            print("\nDEBUG - Job #14:")
            print(f"Header: {header[:200]}...")  # Print first 200 chars
            print(f"Header (lowercase): {header.lower()[:200]}...")
            print(f"Detected Job Types: {job_types}")
            # Print all potential matches found
            header_lower = header.lower()
            print("\nPotential matches found:")
            for keyword in JOB_TYPE_KEYWORDS:
                if keyword.lower() in header_lower:
                    print(f"- Found '{keyword}' in header")

    df = pd.DataFrame(results)
    output_file = Path("2018_Analysis/2018_job_type/2018_job_type_details.xlsx")
    df.to_excel(output_file, index=False)
    print(f"\nSaved job type details to: {output_file}")

if __name__ == "__main__":
    main() 
