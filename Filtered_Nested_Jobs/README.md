# Filtered Nested Job Posts

This directory contains filtered versions of the Hacker News "Who is Hiring?" posts that:
1. Filter out posts with 20 words or less
2. Remove all HTML tags from the posts

## Contents

- `filtered_nested_job_posts.json`: Contains job postings after filtering out short posts (20 words or less), organized by month
- `filtered_nested_job_posts_yearly.json`: Contains job postings after filtering out short posts (20 words or less), organized by year
  - Structure:
  ```json
  {
      "YC": {
          "2012": {
              "comments": ["cleaned job posting 1", "cleaned job posting 2", ...],
              "numJobPost": 1234
          },
          "2013": {
              "comments": [...],
              "numJobPost": ...
          }
      }
  }
  ```

## Scripts

- `filter_short_posts.py`: Filters out short posts (20 words or less) and organizes by month
- `filter_short_posts_yearly.py`: Filters out short posts (20 words or less) and organizes by year

## Statistics

- Total Posts: 82,554
- Time Range: 2012-2024
- Posts per Year: Varies
- Data Format: Cleaned and structured

## Purpose

This filtered dataset is useful for:
- Analyzing job postings of sufficient length
- Studying job descriptions without HTML formatting
- Comparing different lengths of job postings
- Understanding detailed job descriptions
- Analyzing yearly trends in job postings

## Notes

- Filters out posts with 20 words or less
- Removes all HTML tags from posts
- Available in both monthly and yearly formats
- Only includes years that have at least one filtered post
- Preserves the chronological organization of the original data 
