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
        'distributed': 'Remote',
        'virtual': 'Remote',
        'work anywhere': 'Remote',
        'work from anywhere': 'Remote',
        'work remotely': 'Remote',
        'work remote': 'Remote',
        'remote work': 'Remote',
        'remote position': 'Remote',
        'remote role': 'Remote',
        'remote job': 'Remote',
        'remote team': 'Remote',
        'distributed team': 'Remote',
        'virtual team': 'Remote',
        'virtual position': 'Remote',
        'work from home': 'Remote',
        'work at home': 'Remote',
        'home based': 'Remote',
        'home-based': 'Remote',
        'home office': 'Remote',
        'home-office': 'Remote',
        
        'onsite': 'On-site',
        'on site': 'On-site',
        'on-site': 'On-site',
        'local': 'On-site',
        'in office': 'On-site',
        'in-office': 'On-site',
        'in person': 'On-site',
        'in-person': 'On-site',
        'at office': 'On-site',
        'at our office': 'On-site',
        'at our location': 'On-site',
        'at our headquarters': 'On-site',
        'office based': 'On-site',
        'office-based': 'On-site',
        'in house': 'On-site',
        'in-house': 'On-site',
        'in the office': 'On-site',
        'in our office': 'On-site',
        'in our location': 'On-site',
        'in our headquarters': 'On-site',
        
        'full time': 'Full-time',
        'fulltime': 'Full-time',
        'full-time': 'Full-time',
        'permanent': 'Full-time',
        'regular': 'Full-time',
        'staff': 'Full-time',
        'staff position': 'Full-time',
        'staff role': 'Full-time',
        'staff job': 'Full-time',
        
        'part time': 'Part-time',
        'parttime': 'Part-time',
        'part-time': 'Part-time',
        'temporary': 'Part-time',
        'seasonal': 'Part-time',
        'casual': 'Part-time',
        'flexible hours': 'Part-time',
        'flexible schedule': 'Part-time',
        
        'full relocation': 'Must relocate',
        'relocation required': 'Must relocate',
        'then move to': 'Must relocate',
        'need to relocate': 'Must relocate',
        'must be willing to relocate': 'Must relocate',
        'relocation assistance': 'Must relocate',
        'relocation package': 'Must relocate',
        'relocation support': 'Must relocate',
        'relocation benefits': 'Must relocate',
        'relocation expenses': 'Must relocate',
        'relocation costs': 'Must relocate',
        'relocation reimbursement': 'Must relocate',
        'relocation allowance': 'Must relocate',
        'relocation bonus': 'Must relocate',
        
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
        'will sponsor': 'Visa sponsorship available',
        'can sponsor': 'Visa sponsorship available',
        'willing to sponsor': 'Visa sponsorship available',
        'visa available': 'Visa sponsorship available',
        'visa provided': 'Visa sponsorship available',
        'visa support': 'Visa sponsorship available',
        'visa assistance': 'Visa sponsorship available',
        'visa sponsorship available': 'Visa sponsorship available',
        'visa sponsorship provided': 'Visa sponsorship available',
        'visa sponsorship support': 'Visa sponsorship available',
        'visa sponsorship assistance': 'Visa sponsorship available',
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
                                      "remote role", "remote job", "remote team",
                                      "distributed team", "virtual team", "virtual position",
                                      "work anywhere", "work from anywhere",
                                      "work at home", "home based", "home-based",
                                      "home office", "home-office"]):
        found_types.add("Remote")
    
    # Relocation and sponsorship variations
    if any(x in header_lower for x in ["full relocation", "relocation required", 
                                      "must relocate", "then move to", "relocate to",
                                      "need to relocate", "must be willing to relocate",
                                      "relocation assistance", "relocation package",
                                      "relocation support", "relocation benefits",
                                      "relocation expenses", "relocation costs",
                                      "relocation reimbursement", "relocation allowance",
                                      "relocation bonus"]):
        found_types.add("Must relocate")
    
    # Visa sponsorship variations
    if any(x in header_lower for x in ["sponsorship", "visa sponsorship", "visa available", 
                                      "sponsor visa", "visa provided", "h-1b", "h1b", "h1-b",
                                      "h-1bs", "h1bs", "h1-bs", "sponsor h-1b", "sponsor h1b", 
                                      "sponsor h1-b", "sponsor h-1bs", "sponsor h1bs", "sponsor h1-bs",
                                      "will sponsor", "can sponsor", "willing to sponsor",
                                      "visa support", "visa assistance",
                                      "visa sponsorship available", "visa sponsorship provided",
                                      "visa sponsorship support", "visa sponsorship assistance"]):
        found_types.add("Visa sponsorship available")
    
    # Location-based detection
    # Check for explicit on-site mentions first (case-insensitive)
    if re.search(r'\b(?:onsite|on\s*site|on-site|in\s*office|in-office|local(?:\s+only)?|in\s*person|in-person|at\s*office|at\s*our\s*(?:office|location|headquarters)|office\s*based|office-based|in\s*house|in-house|in\s*the\s*office|in\s*our\s*(?:office|location|headquarters))\b', header_lower):
        found_types.add("On-site")
        if "Remote" in found_types:  # Remove remote if explicitly on-site
            found_types.remove("Remote")
    # If no explicit on-site mention, check for location patterns
    elif "Remote" not in found_types:
        # If no job type is found but there are specific locations mentioned, it's likely on-site
        if not found_types and re.search(r'(?:in|at|based in|located in|office in|headquarters in)\s+[A-Za-z\s,]+', header):
            found_types.add("On-site")
        
        # If multiple locations are mentioned with "or", it's likely on-site with multiple options
        if re.search(r'[A-Za-z\s,]+(?:or|/)\s*[A-Za-z\s,]+', header):
            found_types.add("On-site")
    
    # Convert set to sorted list for consistent ordering
    found_types = sorted(list(found_types))
    return " | ".join(found_types) if found_types else "Unknown"

def main():
    # Load posts
    with open("2012_Analysis/2012_job_posts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    posts = data["YC"]["2012"]["comments"]

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

    df = pd.DataFrame(results)
    output_file = Path("2012_Analysis/2012_job_type/2012_job_type_details.xlsx")
    df.to_excel(output_file, index=False)
    print(f"\nSaved job type details to: {output_file}")

if __name__ == "__main__":
    main() 
