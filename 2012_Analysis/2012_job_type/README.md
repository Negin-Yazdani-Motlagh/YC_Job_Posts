# 2012 YC Job Posts - Job Type Analysis

This directory contains the analysis of job types from Y Combinator job posts in 2012. The analysis focuses on categorizing job posts based on various employment characteristics.

## Files

- `extract_job_type.py`: Main script for analyzing job types
- `2012_job_type_details.xlsx`: Excel file containing the analysis results

## Job Type Categories

The script analyzes the following job type categories:

### 1. Work Location
- **Remote**: Work from home, telecommute, distributed team
- **On-site**: Office-based, in-person work
- **Hybrid**: Combination of remote and on-site work

### 2. Employment Type
- **Full-time**: Permanent, regular, staff positions
- **Part-time**: Temporary, seasonal, casual positions
- **Contract**: Freelance, consultant positions
- **Internship**: Paid and unpaid internship positions

### 3. Relocation
- **Must relocate**: Positions requiring relocation
- **Relocation assistance**: Positions offering relocation support
- **Temporary remote**: Remote work with eventual relocation requirement

### 4. Visa Sponsorship
- **Visa sponsorship available**: Positions offering H-1B or other visa sponsorship
- **No sponsorship**: Positions not offering visa sponsorship

## Analysis Features

The script includes:
- Case-insensitive matching
- Multiple job type detection per post
- Context-aware detection
- Location-based inference
- Standardized terminology

## Usage

To run the analysis:
```bash
python extract_job_type.py
```

The script will:
1. Read job posts from `2012_job_posts.json`
2. Analyze each post for job type characteristics
3. Generate an Excel file with the results
4. Display sample results for verification

## Output

The analysis results are saved in `2012_job_type_details.xlsx` with the following columns:
- Post #: Sequential number of the job post
- Job Type: Detected job types separated by " | "

## Notes

- The script uses a comprehensive list of keywords and variations to detect job types
- Location-based detection is used when explicit job type information is not provided
- Multiple job types can be detected for a single post
- Results are normalized to avoid duplicate categories 
