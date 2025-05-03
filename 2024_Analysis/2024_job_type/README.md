# 2024 YC Job Posts - Job Type Analysis

This directory contains the analysis of job types from Y Combinator job posts in 2024. The analysis focuses on categorizing job posts based on various employment characteristics.

## Files

- `extract_job_type.py`: Main script for analyzing job types
- `2024_job_type_details.xlsx`: Excel file containing the analysis results

## Job Type Categories

The script analyzes the following job type categories:

### 1. Work Location
- **Remote**: Work from home, telecommute, distributed team, work anywhere, virtual, remote-first, remote-friendly, remote-optional, work remotely, remote work, work from anywhere in the world, fully remote, 100% remote, remote-first company, globally distributed, remote-forever, remote-by-default, remote-only, remote-native
- **On-site**: Office-based, in-person work, at office location, headquarters, local, in-office, on-premise, in-house, office-based, physical office, office presence required, office-based role, office-first, office-centric
- **Hybrid**: Combination of remote and on-site work, flexible location, partial remote, work from anywhere, flexible work arrangement, work from home option, hybrid remote, flexible remote, hybrid work model, hybrid-first, flexible hybrid, hybrid-by-choice, hybrid-flexible

### 2. Employment Type
- **Full-time**: Permanent, regular, staff positions, salaried, W-2, direct hire, full-time employee, FTE, full-time role, permanent role, full-time position, full-time opportunity, full-time employment, full-time permanent
- **Part-time**: Temporary, seasonal, casual positions, hourly, contract-to-hire, flex-time, part-time employee, PTE, part-time role, flexible hours, part-time position, part-time opportunity, part-time employment, part-time flexible
- **Contract**: Freelance, consultant positions, project-based, 1099, corp-to-corp, independent contractor, contract worker, contract role, temporary role, contract position, contract opportunity, contract employment, contract-based
- **Internship**: Paid and unpaid internship positions, co-op, apprenticeship, summer intern, winter intern, fall intern, intern role, internship program, intern position, internship opportunity, internship employment, internship program

### 3. Relocation
- **Must relocate**: Positions requiring relocation, move to office, relocation required, based in, office location, relocate to, must be willing to relocate, relocation necessary, relocation expected, relocation required, relocation mandatory, relocation essential
- **Relocation assistance**: Positions offering relocation support, package, benefits, expenses, bonus, moving costs, relocation reimbursement, relocation stipend, moving assistance, relocation package available, relocation support provided, relocation benefits, relocation assistance available, relocation package offered
- **Temporary remote**: Remote work with eventual relocation requirement, start remote, remote to start, remote initially, remote during onboarding, remote until relocation, remote first, remote until safe to return, remote until office reopens, remote to start with relocation, remote-first with eventual relocation, remote-to-relocate

### 4. Visa Sponsorship
- **Visa sponsorship available**: Positions offering H-1B or other visa sponsorship, green card, OPT, STEM OPT, TN visa, E-3 visa, visa support available, international candidates welcome, global talent welcome, visa sponsorship provided, visa sponsorship available, visa sponsorship offered
- **No sponsorship**: Positions not offering visa sponsorship, US citizens only, no visa support, US work authorization required, must be authorized to work in US, US work permit required, no visa sponsorship, US-based only, US work authorization needed, US work authorization required, US work authorization mandatory, US work authorization essential

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
- Work authorization requirement detection
- Role-based classification
- Post-pandemic work arrangement detection
- Global work arrangement detection
- Employment type classification
- Work arrangement classification

## Usage

To run the analysis:
```bash
python extract_job_type.py
```

The script will:
1. Read job posts from `2024_job_posts.json`
2. Analyze each post for job type characteristics
3. Generate an Excel file with the results
4. Display sample results for verification

## Output

The analysis results are saved in `2024_job_type_details.xlsx` with the following columns:
- Post #: Sequential number of the job post
- Job Type: Detected job types separated by " | "

## Notes

- The script uses a comprehensive list of keywords and variations to detect job types
- Location-based detection is used when explicit job type information is not provided
- Multiple job types can be detected for a single post
- Results are normalized to avoid duplicate categories
- Enhanced detection for:
  - Remote work variations (work anywhere, work from anywhere, virtual, remote-first, remote-friendly, remote-optional, work remotely, remote work, work from anywhere in the world, fully remote, 100% remote, remote-first company, globally distributed, remote-forever, remote-by-default, remote-only, remote-native)
  - On-site variations (in person, in-person, at office, headquarters, local, in-office, on-premise, in-house, office-based, physical office, office presence required, office-based role, office-first, office-centric)
  - Relocation assistance variations (package, support, benefits, expenses, bonus, moving costs, reimbursement, stipend, moving assistance, relocation package available, relocation support provided, relocation benefits, relocation assistance available, relocation package offered)
  - Visa sponsorship variations (support, assistance, green card, OPT, STEM OPT, TN visa, E-3 visa, visa support available, international candidates welcome, global talent welcome, visa sponsorship provided, visa sponsorship available, visa sponsorship offered)
  - Hybrid work arrangements (flexible location, partial remote, work from anywhere, flexible work arrangement, work from home option, hybrid remote, flexible remote, hybrid work model, hybrid-first, flexible hybrid, hybrid-by-choice, hybrid-flexible)
  - Employment status (W-2, 1099, Corp-to-Corp, direct hire, full-time employee, FTE, full-time role, permanent role, full-time position, full-time opportunity, full-time employment, full-time permanent)
  - Contract variations (contract-to-hire, project-based, flex-time, independent contractor, contract worker, contract role, temporary role, contract position, contract opportunity, contract employment, contract-based)
  - Internship variations (summer intern, winter intern, fall intern, co-op, intern role, internship program, intern position, internship opportunity, internship employment, internship program)
  - Work authorization requirements (must be authorized to work in US, US work permit required, no visa sponsorship, US-based only, US work authorization needed, US work authorization required, US work authorization mandatory, US work authorization essential)
  - Global work arrangements (globally distributed, remote-first company, hybrid-first, remote-forever, remote-by-default, office-first, hybrid-by-choice, remote-only, remote-native, office-centric, hybrid-flexible) 
