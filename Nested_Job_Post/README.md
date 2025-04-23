# Nested Job Posts Data

This directory contains processed data from Hacker News "Who is Hiring?" posts, organized in a structured format with both JSON and Excel outputs.

## Contents

1. `nested_job_posts.json`
   - Contains all job postings organized by month and year
   - Uses month names instead of numbers (e.g., "January" instead of "1")
   - Structure:
   ```json
   {
       "YC": {
           "2012-December": {
               "comments": ["job posting 1", "job posting 2", ...],
               "numJobPost": 123
           },
           "2013-January": {
               "comments": [...],
               "numJobPost": ...
           }
       }
   }
   ```

2. `job_posts_summary.xlsx`
   - Excel file containing summary statistics
   - Columns:
     - Month (full month name)
     - Year
     - Total Job Posts (count of postings for that month)

## Data Processing

The data was processed using the following steps:
1. Reading HTML content from `HTML_who_is_hiring/hiring_posts_html.json`
2. Extracting top-level job postings from each month's thread
3. Cleaning the text content (removing reply/flag links)
4. Organizing by month and year
5. Creating both JSON and Excel outputs

## Statistics

- Time Range: 2012-2024
- Posts per Month: Varies (typically 100-500)
- Total Months: 153
- Data Format: Cleaned and structured

## Usage

The data can be used for:
- Analyzing job posting trends over time
- Comparing posting volumes across months/years
- Studying the evolution of job postings
- Creating visualizations of job market trends

## Notes

- All months are represented by their full names
- Data is sorted chronologically
- Only top-level job postings are included (replies excluded)
- Excel file provides an easy way to analyze posting volumes 
