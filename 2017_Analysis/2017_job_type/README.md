# 2017 YC Job Posts - Job Type Analysis

This directory contains the analysis of job types from Y Combinator job posts in 2017. The analysis focuses on categorizing job posts based on various employment characteristics.

## Files

- `extract_job_type.py`: Main script for analyzing job types
- `2017_job_type_details.xlsx`: Excel file containing the analysis results

## Job Type Categories

The script analyzes the following job type categories:

### 1. Work Location
- **Remote**: Work from home, telecommute, distributed team, work anywhere, virtual, remote-first, remote-friendly, remote-optional
- **On-site**: Office-based, in-person work, at office location, headquarters, local, in-office, on-premise
- **Hybrid**: Combination of remote and on-site work, flexible location, partial remote, work from anywhere, flexible work arrangement

### 2. Employment Type
- **Full-time**: Permanent, regular, staff positions, salaried, W-2, direct hire, full-time employee
- **Part-time**: Temporary, seasonal, casual positions, hourly, contract-to-hire, flex-time, part-time employee
- **Contract**: Freelance, consultant positions, project-based, 1099, corp-to-corp, independent contractor
- **Internship**: Paid and unpaid internship positions, co-op, apprenticeship, summer intern, winter intern

### 3. Relocation
- **Must relocate**: Positions requiring relocation, move to office, relocation required, based in, office location
- **Relocation assistance**: Positions offering relocation support, package, benefits, expenses, bonus, moving costs, relocation reimbursement
- **Temporary remote**: Remote work with eventual relocation requirement, start remote, remote to start, remote initially, remote during onboarding

### 4. Visa Sponsorship
- **Visa sponsorship available**: Positions offering H-1B or other visa sponsorship, green card, OPT, STEM OPT, TN visa
- **No sponsorship**: Positions not offering visa sponsorship, US citizens only, no visa support, US work authorization required, must be authorized to work in US

## Analysis Features

The script includes:
- Case-insensitive matching
- Multiple job type detection per post
- Context-aware detection
- Location-based inference
- Standardized terminology
- Enhanced pattern matching for various job type expressions
- Improved detection of hybrid work arrangements
- Employment status detection (W-2, 1099, Corp-to-Corp)
- Enhanced remote work policy detection
- Flexible work arrangement detection

## Usage

To run the analysis:
```bash
python extract_job_type.py
```

The script will:
1. Read job posts from `2017_job_posts.json`
2. Analyze each post for job type characteristics
3. Generate an Excel file with the results
4. Display sample results for verification

## Output

The analysis results are saved in `2017_job_type_details.xlsx` with the following columns:
- Post #: Sequential number of the job post
- Job Type: Detected job types separated by " | "

## Notes

- The script uses a comprehensive list of keywords and variations to detect job types
- Location-based detection is used when explicit job type information is not provided
- Multiple job types can be detected for a single post
- Results are normalized to avoid duplicate categories
- Enhanced detection for:
  - Remote work variations (work anywhere, work from anywhere, virtual, remote-first, remote-friendly, remote-optional)
  - On-site variations (in person, in-person, at office, headquarters, local, in-office, on-premise)
  - Relocation assistance variations (package, support, benefits, expenses, bonus, moving costs, reimbursement)
  - Visa sponsorship variations (support, assistance, green card, OPT, STEM OPT, TN visa)
  - Hybrid work arrangements (flexible location, partial remote, work from anywhere, flexible work arrangement)
  - Employment status (W-2, 1099, Corp-to-Corp, direct hire, full-time employee)
  - Contract variations (contract-to-hire, project-based, flex-time, independent contractor)
  - Internship variations (summer intern, winter intern, co-op)
  - Work authorization requirements (must be authorized to work in US) 
